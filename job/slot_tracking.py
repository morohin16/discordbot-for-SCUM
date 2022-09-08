import discord
import datetime
import requests
import urllib.parse
import logging

async def run(logging: logging, bot: discord.Client,server_id: str) :
    server_url = "https://api.battlemetrics.com/servers/{0}".format(server_id)

    info_response = requests.get(server_url)
    if info_response.status_code == 200:
      info = info_response.json()['data']['attributes']
      status_flag   = discord.Status.online if info['status'] == 'online' else  discord.Status.dnd
      online        = info['players']
      max           = info['maxPlayers']

      status_name = "🙋{0}/{1}".format(online,max)
      await bot.change_presence(status=status_flag, activity=discord.Activity(type=discord.ActivityType.playing, name=status_name))
      logging.info(
        "data updated! : {0} \"{1}\""
        .format(str(status_flag)
        .replace(str(discord.Status.dnd),"offline")
        ,status_name))
def encode_time(datetime: datetime.datetime) : 
    return urllib.parse.quote(datetime.strftime("%Y-%m-%dT%H:%M:%S.000Z"))