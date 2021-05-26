import discord
import os
import typing
import asyncio
from keep_alive import keep_alive
from discord.ext import commands
import requests
import aiohttp


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)
async def on_ready():
  print("I'm in")
  print(bot.user)
  await bot.change_presence(activity=discord.Game("!help | Playing Brawl Stars"))

# @bot.event
# async def on_message(message):
#   #auto respond & prefixless commands
#   if not message.author.bot and message.author != bot.user:
#     if bot.user.mentioned_in(message):
#         await message.channel.send('Hello! My prefix is `b!` and my help command is, `b!help`!')

brawl_stars_api_key = 'api key is retrievable at developer.brawlstars.com'

@bot.command()
async def player(message, id: str):
  """Get Player Statistics!"""
  url = f'https://api.brawlstars.com/v1/players/%23{id}'
  headers={'Authorization' :f'Bearer {brawl_stars_api_key}'}
  results = requests.get(url=url, headers=headers).json()
  name = results["name"]
  tag = results["tag"]
  trophies = results["trophies"]
  most_trophies = results["highestTrophies"]
  most_power_play_points = results["highestPowerPlayPoints"]
  xp_lvl = results["expLevel"]
  xp_points = results["expPoints"]
  qualified_from_championship_challenge = results["isQualifiedFromChampionshipChallenge"]
  victory_3v3 = results["3vs3Victories"]
  victory_solo = results["soloVictories"]
  victory_duo = results["duoVictories"]
  best_roborumble = results["bestRoboRumbleTime"]
  best_bigbrawler = results["bestTimeAsBigBrawler"]
  club_tag = results["club"]["tag"]
  club_name = results["club"]["name"]
  brawler_count = len(results["brawlers"])

  dogfact = discord.Embed(title=f'Brawl Stars Statistics for {name}', description=f'Player ID: {tag}\nXP Level: {xp_lvl}\nAmount of XP: {xp_points}', color=discord.Color.blue())
  dogfact.add_field(name='Player Statistics!', value=f'Trophies: {trophies}\nMost Trophies: {most_trophies}\nMost Power Play Points: {most_power_play_points}\nBrawler Count: {brawler_count}\nChampionship Qualification: {qualified_from_championship_challenge}', inline=True)
  dogfact.add_field(name='Wins!', value=f'Solo Victories: {victory_solo}\nDuo Victories: {victory_duo}\n3v3 Victories: {victory_3v3}\nBest Robo Rumble Time: {best_roborumble}\nBest Time as Big Brawler: {best_bigbrawler}', inline=True)
  dogfact.add_field(name='Club!', value=f'Club: {club_name}\nClub Tag: {club_tag}', inline=True)
  await message.send(embed=dogfact)

# @bot.command()
# async def ranking(message, rank_type: str, country_code: str):
#   """Get Ranking for a club, powerplay, brawler, and players in a specific country or global!"""
#   rank_type_lower = rank_type.lower()
#   if rank_type_lower == 'powerplay':
#     await message.send(f'hi')
#   elif rank_type_lower == 'club':
#     await message.send(f'hi')
#   elif rank_type_lower == 'player':
#     await message.send(f'hi')
#   elif rank_type_lower == 'powerplay'
#     url = f'https://api.brawlstars.com/v1/players/%23{id}'
#     headers={'Authorization' :f'Bearer {brawl_stars_api_key}'}
#     results = requests.get(url=url, headers=headers).json()
#     name = results["name"]

#     dogfact = discord.Embed(title=f'Brawl Stars Statistics for {name}', description=f'Player ID: {tag}\nXP Level: {xp_lvl}\nAmount of XP: {xp_points}', color=discord.Color.blue())
#     dogfact.add_field(name='Player Statistics!', value=f'Trophies: {trophies}\nMost Trophies: {most_trophies}\nMost Power Play Points: {most_power_play_points}\nBrawler Count: {brawler_count}\nChampionship Qualification: {qualified_from_championship_challenge}', inline=True)
#     dogfact.add_field(name='Wins!', value=f'Solo Victories: {victory_solo}\nDuo Victories: {victory_duo}\n3v3 Victories: {victory_3v3}\nBest Robo Rumble Time: {best_roborumble}\nBest Time as Big Brawler: {best_bigbrawler}', inline=True)
#     dogfact.add_field(name='Club!', value=f'Club: {club_name}\nClub Tag: {club_tag}', inline=True)
#     await message.send(embed=dogfact)

@bot.command()
async def club(message, id: str):
  """Get Club Statistics!"""
  url = f'https://api.brawlstars.com/v1/clubs/%23{id}'
  headers={'Authorization' :f'Bearer {brawl_stars_api_key}'}
  results = requests.get(url=url, headers=headers).json()
  name = results["name"]
  tag = results["tag"]
  c_type = results["type"]
  description = results["description"]
  required_trophies = results["requiredTrophies"]
  total_trophies = results["trophies"]
  member_count = len(results["members"])

  first_member_name = results["members"][0]["name"]
  first_member_tag = results["members"][0]["tag"]
  first_member_trophies = results["members"][0]["trophies"]
  first_member_role = results["members"][0]["role"]

  second_member_name = results["members"][1]["name"]
  second_member_tag = results["members"][1]["tag"]
  second_member_trophies = results["members"][1]["trophies"]
  second_member_role = results["members"][1]["role"]

  third_member_name = results["members"][2]["name"]
  third_member_tag = results["members"][2]["tag"]
  third_member_trophies = results["members"][2]["trophies"]
  third_member_role = results["members"][2]["role"]

  fourth_member_name = results["members"][3]["name"]
  fourth_member_tag = results["members"][3]["tag"]
  fourth_member_trophies = results["members"][3]["trophies"]
  fourth_member_role = results["members"][3]["role"]

  fifth_member_name = results["members"][4]["name"]
  fifth_member_tag = results["members"][4]["tag"]
  fifth_member_trophies = results["members"][4]["trophies"]
  fifth_member_role = results["members"][4]["role"]
  
  dogfact = discord.Embed(title=f'Brawl Stars Club Statistics for {name}', description=f'Description: {description}', color=discord.Color.blue())
  dogfact.add_field(name='Club Statistics!', value=f'Club Tag: {tag}\nTotal Trophies: {total_trophies}\nRequired Trophies: {required_trophies}\nClub Status: {c_type}\nMember Count: {member_count}', inline=True)
  dogfact.add_field(name='1st Place!', value=f'Name: {first_member_name}\nTag: {first_member_tag}\nRole: {first_member_role}\nTrophies: {first_member_trophies}', inline=False)
  dogfact.add_field(name='2nd Place!', value=f'Name: {second_member_name}\nTag: {second_member_tag}\nRole: {second_member_role}\nTrophies: {second_member_trophies}', inline=False)
  dogfact.add_field(name='3rd Place!', value=f'Name: {third_member_name}\nTag: {third_member_tag}\nRole: {third_member_role}\nTrophies: {third_member_trophies}', inline=False)
  dogfact.add_field(name='4th Place!', value=f'Name: {fourth_member_name}\nTag: {fourth_member_tag}\nRole: {fourth_member_role}\nTrophies: {fourth_member_trophies}', inline=False)
  dogfact.add_field(name='5th Place!', value=f'Name: {fifth_member_name}\nTag: {fifth_member_tag}\nRole: {fifth_member_role}\nTrophies: {fifth_member_trophies}', inline=False)
  await message.send(embed=dogfact)

keep_alive()
token = "token"
bot.run(token)
