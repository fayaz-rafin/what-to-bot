import token
import discord
import os
import random
from discord.ext import commands
from discord import embeds
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
async def wheretogo(ctx, message):
    with open('places.json') as f:
        places = json.load(f)
        ran = random.randint(0, 5)
        name = places[f'{message}'][ran]["name"]
        pic = places[f'{message}'][ran]["pic"]
        descrip = places[f'{message}'][ran]["description"]
        embed = discord.Embed(title=name, description=descrip, color=0xFF5733)
        embed.set_image(url=pic)
        await ctx.send(embed=embed)


@client.command()
async def whattowatch(ctx):
    with open('movie.json') as f:
        movie = json.load(f)
        ran = random.randint(0, 2)
        name = movie["Movie"][ran]["name"]
        pic = movie["Movie"][ran]["pic"]
        descrip = movie["Movie"][ran]["description"]
        embed = discord.Embed(title=name, description=descrip, color=0xFF5733)
        embed.set_thumbnail(url=pic)
        await ctx.send(embed=embed)


@client.command()
async def whattocook(ctx, message):
    with open('food.json') as f:
        data = json.load(f)
        ran = random.randint(0, 3)
        name = data[f'{message}'][ran]["name"]
        url = data[f'{message}'][ran]["url"]
        pic = data[f'{message}'][ran]["pic"]
        serving = data[f'{message}'][ran]["servings"]

        embed = discord.Embed(
            title=name,
            url=url,
            #  description=
            #  serving,
            color=0xfce188)
        #embed.set_thumbnail(url=pic)
        embed.set_image(url=pic)
      
        embed.add_field(name=serving, value=url, inline=False)
        #embed.set_footer(text='blah blah')

    await ctx.send(embed=embed)

@client.command()
async def whattolisten(ctx):
    with open('music.json') as f:
      music = json.load(f)
      ran = random.randint(0,3)
      name = music["Music"][ran]["name"]
      artist = music["Music"][ran]["artist"]
      url = music["Music"][ran]["url"]
      embed = discord.Embed(title=name,url=url,description=artist,color=0xfce188)
      embed.add_field(name="Song URL:", value=url, inline=False)
      #embed.set_image(url=url)
      await ctx.send(embed=embed)

@client.command()
async def Help(ctx):
  embed = discord.Embed(title="Bot Commands",description="Here's what i can do: Type 'whattocook {Food, Dessert, Drink}' for food reccomendations. Type 'whattowatch' to watch something when you're bored to find show reccomendations. Type 'whattolisten' to get song reccomendations and spice up your playlist. Type 'wheretogo' to get help deciding where to plan your next hangout", color=0xfce188)
  
  
  await ctx.send(embed=embed)
  

      
      

client.run(os.getenv("TOKEN"))
