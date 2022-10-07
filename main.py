import discord
import os
from discord.ext import commands, tasks
# TOKEN
from dotenv import load_dotenv
load_dotenv()
#API
import requests
#DELAY
import asyncio

# TOKEN
TOKEN = os.getenv('TOKEN')
print(TOKEN)

#API KEY
api_key = os.getenv('API_KEY')
print(api_key)

#TASK:
# 1. send data
# 2. stop data

#Start API
api_url = "https://eun1.api.riotgames.com/lol/challenges/v1/challenges/config" # 325 index id
api_url = api_url + '?api_key=' + api_key
resp = requests.get(api_url)
print(resp) # Response 200
data = resp.json()

#Start Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents,help_command=None)

# on_ready command 
@bot.event
async def on_ready():
 print('{0.user} connect to your channel!'.format(bot))
#  channel = bot.get_channel(1014874558366502925) # channel ID
#  await channel.send(' {0.user} connect to your channel!'.format(bot))
#  await channel.send('Key !help to Command Manual')

# Stop 
@bot.command()
async def stop(ctx):
 data.stop()
 await ctx.send("**stop data**")


# Play
@bot.command()
async def play(ctx):
  await ctx.send("**play data**")
  data.start(ctx)
 
  
  
#  embed=discord.Embed(title = 'Data API',color = discord.Color.blue())
 
#  embed.add_field(name='id', value = data[0]['id'], inline=False) # id
#    # embed.add_field(name='name', value = data[x]['localizedNames']['en_US']['name'], inline=False) # localizedNames -> name
#    # embed.add_field(name='description', value = data[x]['localizedNames']['en_US']['shortDescription'], inline=False) # localizedNames -> description
#    # embed.add_field(name='IRON', value = data[x]['thresholds']['IRON'], inline=False) # thresholds -> IRON
#    # embed.add_field(name='GOLD', value = data[x]['thresholds']['GOLD'], inline=False) # thresholds -> GOLD
#    # embed.add_field(name='SILVER', value = data[x]['thresholds']['SILVER'], inline=False) # thresholds -> SILVER
#    # embed.add_field(name='DIAMOND', value = data[x]['thresholds']['DIAMOND'], inline=False) # thresholds -> DIAMOND
#    # embed.add_field(name='BRONZE', value = data[x]['thresholds']['BRONZE'], inline=False) # thresholds -> BRONZE
#    # embed.add_field(name='PLATINUM', value = data[x]['thresholds']['PLATINUM'], inline=False) # thresholds -> PLATINUM
#    # embed.add_field(name='MASTER', value = data[x]['thresholds']['MASTER'], inline=False) # thresholds -> MASTER
#    # embed.add_field(name='new player', value ='wait for new data', inline=False) # new id
#  await ctx.send(embed=embed)
#  await asyncio.sleep(3)

@tasks.loop()
async def data(ctx):

 data = resp.json()

 for x in range(325):
  embed=discord.Embed(title = 'Data API for Player ' + str(x) ,color = discord.Color.red())
  embed.add_field(name='id', value = data[x]['id'], inline=False) # id
  embed.add_field(name='name', value = data[x]['localizedNames']['en_US']['name'], inline=False) # localizedNames -> name
  embed.add_field(name='description', value = data[x]['localizedNames']['en_US']['shortDescription'], inline=False) # localizedNames -> description
  embed.add_field(name='IRON', value = data[x]['thresholds']['IRON'], inline=False) # thresholds -> IRON
  embed.add_field(name='GOLD', value = data[x]['thresholds']['GOLD'], inline=False) # thresholds -> GOLD
  embed.add_field(name='SILVER', value = data[x]['thresholds']['SILVER'], inline=False) # thresholds -> SILVER
  embed.add_field(name='DIAMOND', value = data[x]['thresholds']['DIAMOND'], inline=False) # thresholds -> DIAMOND
  embed.add_field(name='BRONZE', value = data[x]['thresholds']['BRONZE'], inline=False) # thresholds -> BRONZE
  embed.add_field(name='PLATINUM', value = data[x]['thresholds']['PLATINUM'], inline=False) # thresholds -> PLATINUM
  embed.add_field(name='MASTER', value = data[x]['thresholds']['MASTER'], inline=False) # thresholds -> MASTER
  await ctx.send(embed=embed)
  await asyncio.sleep(3)

 
# Help -> Command Manual
@bot.command(name='help')
async def help(ctx):
  embed = discord.Embed(
    title = 'Command Manual',
    color = discord.Color.green()
  )
  # play
  embed.add_field(name='!play', value='send data', inline=False)
  # stop
  embed.add_field(name='!stop', value='stop send data', inline=False)
  await ctx.send(embed=embed)


bot.run(TOKEN)

#  await try1(ctx)
# @bot.event
# async def try1(ctx):
#   await ctx.send("try1")
#   data = resp.json()
#   guild = bot.get_guild(1014874558366502922)
#   channel = bot.get_channel(1014874558366502925) # channel ID
#   for x in range(10):
#    await channel.send('id: ' + str(data[(x)]['id']))


# await channel.send('id: ' + str(data[(x)]['id']))
# await channel.send('name: ' + str(data[x]['localizedNames']['en_US']['name']))

#    guild = bot.get_guild(1014874558366502922)
#  channel = bot.get_channel(1014874558366502925) # channel ID