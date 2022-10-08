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

#API KEY
api_key = os.getenv('API_KEY')

#Start API
api_url = "https://eun1.api.riotgames.com/lol/challenges/v1/challenges/config" 
api_url = api_url + '?api_key=' + api_key
resp = requests.get(api_url)
print(resp) # Response 200
data = resp.json()

#Start Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents,help_command=None)

# on_ready 
@bot.event
async def on_ready():
 print('{0.user} connect to your channel!'.format(bot))
 channel = bot.get_channel(1014874558366502925) # channel ID
 await channel.send(' {0.user} connect to your channel!'.format(bot))
 await channel.send('Key !help to Command Manual or !play to start send data')

# Stop 
@bot.command()
async def stop(ctx):
 await ctx.send("**stop data**")
 data.stop(ctx)
 
# Play
@bot.command()
async def play(ctx):
  await ctx.send("**send data**")
  data.start(ctx)
 
# Loop of Data
@tasks.loop()
async def data(ctx):
 data = resp.json()
 for x in range(325): # 325 index of id
   embed=discord.Embed(title = 'Data API for Player ' + str(x) ,color = discord.Color.red())
   embed.add_field(name='ID', value = data[x]['id'], inline=False) # id
   embed.add_field(name='Name', value = data[x]['localizedNames']['en_US']['name'], inline=False) # localizedNames -> name
   embed.add_field(name='Description', value = data[x]['localizedNames']['en_US']['shortDescription'], inline=False) # localizedNames -> description 
   # All Ranks in League of Legends:
   embed.add_field(name='IRON', value = data[x].get('thresholds', {}).get('IRON'), inline=False) # thresholds -> IRON
   embed.add_field(name='BRONZE', value = data[x].get('thresholds', {}).get('BRONZE'), inline=False) # thresholds -> BRONZE
   embed.add_field(name='SILVER', value = data[x].get('thresholds', {}).get('SILVER'), inline=False) # thresholds -> SILVER
   embed.add_field(name='GOLD', value = data[x].get('thresholds', {}).get('GOLD'), inline=False) # thresholds -> GOLD
   embed.add_field(name='PLATINUM', value = data[x].get('thresholds', {}).get('PLATINUM'), inline=False) # thresholds -> PLATINUM
   embed.add_field(name='DIAMOND', value = data[x].get('thresholds', {}).get('DIAMOND'), inline=False) # thresholds -> DIAMOND
   embed.add_field(name='MASTER', value = data[x].get('thresholds', {}).get('MASTER'), inline=False) # thresholds -> MASTER
   embed.add_field(name='GRANDMASTER', value = data[x].get('thresholds', {}).get('GRANDMASTER'), inline=False) # thresholds -> GRANDMASTER
   embed.add_field(name='CHALLENGER', value = data[x].get('thresholds', {}).get('CHALLENGER'), inline=False) # thresholds -> CHALLENGER
   await ctx.send(embed=embed)
   await asyncio.sleep(3) # Delay
 
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
