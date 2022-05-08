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


#bs-------------------------------------------------------------------------


# return(moviee)
@client.command()
async def movie(ctx, message):
  response = requests.get("http://img.omdbapi.com/?apikey=[yourkey]&")

  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  moviee = json_data[0]
  await message.ctx.send(moviee)


#bs-------------------------------------------------------------------------


@client.command()
async def wheretogo(ctx, message):
    with open('main/places.json') as f:
        places = json.load(f)
        ran = random.randint(0, 5)
        name = places[f'{message}'][ran]["name"]
        pic = places[f'{message}'][ran]["pic"]
        descrip = places[f'{message}'][ran]["description"]
        embed = discord.Embed(title=name, description=descrip, color=0xFF5733)
        embed.set_image(url=pic)
        await ctx.send(embed=embed)


@client.command()
async def whattocook(ctx, message):
    with open('main/food.json') as f:
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


client.run(os.getenv("TOKEN"))
