import discord
import asyncio
import os, sys
import time
from bs4 import BeautifulSoup
from collections import Collection
import info
from configparser import ConfigParser
import datetime

#
# Broadcast | 공지
#
# Prefix 와 token, devid 등 사용자정보는 info.py 에서 변경가능합니다.
# Prefix 설정시 `□□야 ` 와 같이 `□□야` 한 다음 한번 띄어쓰기를 꼭 쓰셔야합니다. 쓰지 않으실 시 작동하지 않습니다.
#
# 제작자 또는 문의 : NAVER#0001
#

def restart():
    os.execl(sys.executable, sys.executable, * sys.argv)

token = info.token()
prefix= info.prefix()
idlist=[]
devid = info.devid()
config = ConfigParser()
playing_msg = "크바야 도와줘 를 입력해보세요!"
restart_playing_msg = "봇 재시작중..."
stop_playing_msg = "봇 종료중..."

class db(discord.Client):
    async def on_ready(self):
        print("Ready !! \n\n=====")
        await client.change_presence(activity=discord.Game(name=playing_msg))
    async def on_message(self, message):
        if message.author.bot:
            pass
        if message.content.startswith(prefix):
            if message.content == prefix:
                pass

            if message.content == prefix+"도와줘":
                embed=discord.Embed(title="", description="아직 없습니다. 왜냐하면 베타에요.")
                await message.channel.send(embed=embed)

            ##### 서버 관련
            if message.content == prefix+"핑":
                nowasdf = datetime.datetime.now()
                await message.channel.trigger_typing()
                latertime = datetime.datetime.now()            
                ping = latertime - nowasdf

                asdf = str(int(ping.microseconds) / 1000)
                asdf = asdf.split(".")
                asdf = asdf[0]
                await message.channel.send(message.author.mention+", %s ms" % asdf)

            ##### 관리자 명령어
            if message.content == prefix+"재시작":
                if str(message.author.id) == devid:
                    await client.change_presence(activity=discord.Game(name=restart_playing_msg))
                    await message.channel.send("재시작함")
                    restart()
                else:
                    await message.channel.send("뿜뿜 안되욧")

            if message.content == prefix+"종료":
                if str(message.author.id) == devid:
                    await client.change_presence(activity=discord.Game(name=stop_playing_msg))
                    await message.channel.send("종료함")
                    await client.close()
                else:
                    await message.channel.send("뿜뿜 안되욧")

client = db()
client.run(token)
                
