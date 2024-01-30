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
ec2 = boto3.client('ec2', region_name=AWS_REGION)

@bot.command(name='start')
async def start_instance(ctx):
    try:
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        response = f'Instance palworld has been started.'
        #response = "Hello world"
    except Exception as e:
        response = f'Error: {e}'
    
    await ctx.send(response)

@bot.command(name='stop')
async def stop_instance(ctx):
    try:
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        response = f'Instance palworld has been stoped.'
        #response = "Hello world"
    except Exception as e:
        response = f'Error: {e}'
    
    await ctx.send(response)

# ボットを実行
#print(TOKEN,AWS_REGION, INSTANCE_ID)
bot.run(TOKEN)
