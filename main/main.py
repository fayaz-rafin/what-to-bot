import token
import discord
import os
import random
from discord.ext import commands
from discord import embeds
import aiohttp
import requests
import json

client = commands.Bot(description="test", command_prefix="$")

@client.event
async def on_ready():
    print("I'm powered up and ready to go!")

client.run('OTcyNTEzNzUwNjgwNzM5ODQx.YnaKAg.zJxUH6_wgF4dZN4hvPmDE2TbSOU')



