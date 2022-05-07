import token
import discord
import os
import random
from discord.ext import commands
from discord import embeds
import aiohttp
import requests
import json
from dotenv import load_dotenv
load_dotenv()


client = commands.Bot(description="test", command_prefix="$")

@client.event
async def on_ready():
    print("I'm powered up and ready to go!")

client.run (os.getenv("TOKEN"))


