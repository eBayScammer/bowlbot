import discord
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(game=discord.Game(name="say bowl"))

@client.event
async def on_message(message):
    if message.author.id != client.user.id and "bowl" in message.content:
        await client.send_message(message.channel, message.content.replace("bowl", "<:bowlcut:492887126820651028>"))
        await client.delete_message(message)

client.run(os.getenv('TOKEN'))
