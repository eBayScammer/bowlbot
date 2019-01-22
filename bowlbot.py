import discord
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import commands
import asyncio
import time
import os
import random

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
    elif message.author.id != client.user.id and "max" in message.content:
        await client.send_message(message.channel, message.content.replace("max", "<:max:536609206829056014>"))
        await client.delete_message(message)
    elif message.content.startswith("!version"):
        emb = (discord.Embed(description="-Added this thing", colour=0x3DF270))
        emb.set_author(name="Version 0.4.2", icon_url='https://i.kym-cdn.com/photos/images/original/001/288/150/85a.jpg')
        await client.send_message(message.channel, embed=emb)
    elif message.content.startswith("!8"):
        await client.send_message(message.channel, random.choice(["It is certain",
                                                                  "It is decidedly so",
                                                                  "Very doubtful",
                                                                  "Concentrate and ask again"]))     
        
client.run(os.getenv('TOKEN'))
