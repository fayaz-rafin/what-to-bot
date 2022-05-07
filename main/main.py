import token
import discord
import os
import random
from discord.ext import commands
from discord import embeds
import aiohttp
import requests
import json
import pprint
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
client = commands.Bot(description="test", command_prefix="$")

@client.event
async def on_ready():
    print("I'm powered up and ready to go!")

@client.command()
async def cook(ctx):
    with open('main/food.json') as f:
        data = json.load(f)
        name = data['Food']
        await ctx.send(name)







client.run (os.getenv("TOKEN"))


