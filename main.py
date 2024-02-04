import os
import discord
import boto3
from discord.ext import commands

# 環境変数から認証情報を取得
TOKEN = os.getenv('DISCORD_TOKEN')
AWS_REGION = os.getenv('AWS_REGION')
INSTANCE_ID = os.getenv('AWS_INSTANCE_ID')

# Discordのクライアントを設定
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# AWS EC2クライアントの初期化
#ec2 = boto3.client('ec2', region_name=AWS_REGION)
ec2 = boto3.resource("ec2", region_name=AWS_REGION)
instance = ec2.Instance(INSTANCE_ID)

@bot.command(name='start')
async def start_instance(ctx):
    try:
        instance.start()
        instance.wait_until_running()
        ip = instance.public_ip_address
        response = f'Instance palworld has been started.\n Please Login through {ip}:8211'
    except Exception as e:
        response = f'Error: {e}'
    
    await ctx.send(response)

@bot.command(name='stop')
async def stop_instance(ctx):
    try:
        instance.stop()
        instance.wait_until_stopped()
        response = f'Instance palworld has been stoped.'
        #response = "Hello world"
    except Exception as e:
        response = f'Error: {e}'
    
    await ctx.send(response)

# ボットを実行
#print(TOKEN,AWS_REGION, INSTANCE_ID)
bot.run(TOKEN)
