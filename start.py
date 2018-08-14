import discord
import asyncio
import os, sys
import time
from bs4 import BeautifulSoup
#from collections import Collection
import info
from configparser import ConfigParser
import datetime
import json
import requests
import random

#
# Broadcast | 공지
#
# Prefix 와 token, devid 등 사용자정보는 info.py 에서 변경가능합니다.
# Prefix 설정시 `□□야 ` 와 같이 `□□야` 한 다음 한번 띄어쓰기를 꼭 쓰셔야합니다. 쓰지 않으실 시 작동하지 않습니다.
#
# 제작자 또는 문의 : NAVER#0001 | BGM#
#
#로그기능 사용법 log(prefix+"명령어, message.author, message.guild.name, message.guild.id, message.content")
#안되있는건 알아서 해주세요

def restart():
    os.execl(sys.executable, sys.executable, * sys.argv)

def log(command, author, servername, serverid, message):
    return print(str(command)+" | "+str(author)+" | "+str(servername)+" | "+str(serverid)+": "+str(message))

token = info.token()
prefix= info.prefix()
nospaceprefix = info.prefix().replace(' ', '')
idlist=[]
devid = info.devid()
config = ConfigParser()
youtube_datakey = info.youtube_datakey()
playing_msg = "크바야 도와줘 를 입력해보세요!"
restart_playing_msg = "봇 재시작중..."
stop_playing_msg = "봇 종료중..."
afklist = []

class db(discord.Client):
    async def on_ready(self):
        print("Ready !! \n\n=====")
        global botstarttime
        botstarttime = datetime.datetime.now()
        await client.change_presence(activity=discord.Game(name=playing_msg))
    async def on_message(self, message):
        if message.author.bot:
            pass

        if message.author.id in afklist:
            await message.channel.send("짜쟌! "+message.author.mention+" 님이 잠수에서 깨어났어요!")
            afklist.remove(message.author.id)

        ##### prefix를 무시받고 하는 부분
        #if message.content == "@someone" or message.content == "@아무나": #오프라인 불가능기능
        #    list=[]
        #    try:
        #        for a in message.guild.members:
        #            if a.status == discord.Status.offline:
        #                pass
        #            else:
        #                list.append(a)
        #        result=str(random.choice(list))
        #        await message.channel.send("** _(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ. o ･ ｡ﾟ_  _%s_**" % result)
        #    except:
        #        await message.channel.send("** _(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ. o ･ ｡ﾟ_  _%s_**" % message.author)

        if message.content == "@someone" or message.content == "@아무나" or message.content == "@섬원" or message.content == "@서먼": #이기능은 맨션도배 위험으로 쿨타임지정해야함. DB작업필요.
            list=[]
            try:
                for a in message.guild.members:
                    list.append(a)
                result=str(random.choice(list))
                await message.channel.send("** _(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ. o ･ ｡ﾟ_            _%s_**" % result)
                log('@someone, @아무나, @섬원, @서먼', message.author, message.guild.name, message.guild.id, message.content)
            except:
                await message.channel.send("** _(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ. o ･ ｡ﾟ_            _%s_**" % message.author)
                log('@someone, @아무나, @섬원, @서먼', message.author, message.guild.name, message.guild.id, message.content)
 
        ##### prefix 또는 nospaceprefix 를 꼭 사용하는 부분
        if message.content.startswith(prefix) or message.content.startswith(nospaceprefix):
            if message.content == nospaceprefix:
                a = ['안녕하세요','왜용?','?','뭐용?!','(╯°□°）╯︵ ┻━┻ 이얍 필살기','MENTION POEWRRRRRR '+message.author.mention,'ㅗㅜㅑ','ㅇ?','!','ㅁㄴㅇㄹ','`'+prefix+"도와줘` 를 쳐보렴. 그러면 날 가지고 놀수있어.",'훗','풉키풉키','ㅍㅋㅍㅋ','아직 배우고 있다고오!','심심해여','맨션빔 맞아보실?','ㅁ?','ㅁ!!!!!']
                a = random.choice(a)
                await message.channel.send(a)
                log(prefix+", "+nospaceprefix, message.author, message.guild.name, message.guild.id, message.content)

            if message.content.startswith(prefix+"유튜브"):
                if message.content[7:] == "":
                    await message.channel.send(message.author.mention+", 검색할 제목을 입력해주세요! >.<")
                else:
                    a = message.content
                    a = a[8:]
                    await message.channel.send(message.author.mention+", `"+a+"` 에 대하여 검색했어요!")
                    global aad
                    aad = message.content[7:]
                    aad = aad.replace(" ", "%20")
                    global bbd
                    bbd = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q='+aad+'&key='+youtube_datakey)
                    global ccd
                    ccd = bbd.text
                    try:
                        ab = json.loads(ccd)["items"][0]["snippet"]["title"]
                    except:
                        pass
                    try:
                        ac = json.loads(ccd)["items"][1]["snippet"]["title"]
                    except:
                        pass
                    try:
                        ad = json.loads(ccd)["items"][2]["snippet"]["title"]
                    except:
                        pass
                    try:
                        ae = json.loads(ccd)["items"][3]["snippet"]["title"]
                    except:
                        pass
                    try:
                        af = json.loads(ccd)["items"][4]["snippet"]["title"]
                    except:
                        pass
                    try:
                        ab1 = json.loads(ccd)["items"][0]["id"]["videoId"]
                    except:
                        pass
                    try:
                        ac1 = json.loads(ccd)["items"][1]["id"]["videoId"]
                    except:
                        pass
                    try:
                        ad1 = json.loads(ccd)["items"][2]["id"]["videoId"]
                    except:
                        pass
                    try:
                        ae1 = json.loads(ccd)["items"][3]["id"]["videoId"]
                    except:
                        pass
                    try:
                        af1 = json.loads(ccd)["items"][4]["id"]["videoId"]
                    except:
                        pass
                    #await message.channel.send("**[1]** "+ab+"\n**[2]** "+ac+"\n**[3]** "+ad+"\n**[4]** "+ae+"\n**[5]** "+af)
                    embed=discord.Embed()
                    num = 0
                    try:
                        num = num + 1
                        embed=embed.add_field(name=ab, value="https://www.youtube.com/watch?v="+ab1)
                    except:
                        num = num - 1
                        pass
                    try:
                        num = num + 1
                        embed=embed.add_field(name=ac, value="https://www.youtube.com/watch?v="+ac1)
                    except:
                        num = num - 1
                        pass
                    try:
                        num = num + 1
                        embed=embed.add_field(name=ad, value="https://www.youtube.com/watch?v="+ad1)
                    except:
                        num = num - 1
                        pass
                    try:
                        num = num + 1
                        embed=embed.add_field(name=ae, value="https://www.youtube.com/watch?v="+ae1)
                    except:
                        num = num - 1
                        pass
                    try:
                        num = num + 1
                        embed=embed.add_field(name=af, value="https://www.youtube.com/watch?v="+af1)
                    except:
                        num = num - 1
                        pass
                    embed = embed.set_footer(text="최대 5 개의 결과 중 "+str(num)+" 개의 검색결과 입니다.")
                    await message.channel.send(embed=embed)
                    log(prefix+"유튜브", message.author, message.guild.name, message.guild.id, message.content)
                
            if message.content.startswith(prefix+"가위바위보") or message.content.startswith(prefix+"가바보") or message.content.startswith(prefix+"짱깽뽀") or message.content.startswith(prefix+"주먹가위보"):
                if message.content[9:] == "" or message.content[7:] == "":
                    await message.channel.send(message.author.mention+" `가위`, `바위`, `보` 중 하나를 선택해줘! `예시) "+prefix+"가위바위보 가위`")
                else:
                    a = ["가위","바위","보"]
                    a = random.choice(a)
                    b = message.content[9:]
                    b = b.replace(" ", "")
                    c = message.content[7:]
                    c = c.replace(" ", "")
                    try:
                        if b == "가위":
                            if a == "가위":
                                await message.channel.send(message.author.mention+", 봇: `가위`, 당신: `가위` | 비겼습니다.")
                            elif a == "바위":
                                await message.channel.send(message.author.mention+", 봇: `바위`, 당신: `가위` | 당신이 졌습니다.")
                            elif a == "보":
                                await message.channel.send(message.author.mention+", 봇: `보`, 당신: `가위` | 당신이 이겼습니다.")
                        elif b == "바위":
                            if a == "가위":
                                await message.channel.send(message.author.mention+", 봇: `가위`, 당신: `바위` | 당신이 이겼습니다.")
                            elif a == "바위":
                                await message.channel.send(message.author.mention+", 봇: `바위`, 당신: `바위` | 비겼습니다.")
                            elif a == "보":
                                await message.channel.send(message.author.mention+", 봇: `보`, 당신: `바위` | 당신이 졌습니다.")
                        elif b == "보":
                            if a == "가위":
                                await message.channel.send(message.author.mention+", 봇: `가위', 당신: `보` | 당신이 졌습니다.")
                            elif a == "바위":
                                await message.channel.send(message.author.mention+", 봇: `바위`, 당신: `보` | 당신이 이겼습니다.")
                            elif a == "보":
                                await message.channel.send(message.author.mention+", 봇: `보`, 당신: `보` | 비겼습니다.")
                        elif c == "가위":
                            if a == "가위":
                                await message.channel.send(message.author.mention+", 봇: `가위`, 당신: `가위` | 비겼습니다.")
                            elif a == "바위":
                                await message.channel.send(message.author.mention+", 봇: `바위`, 당신: `가위` | 당신이 졌습니다.")
                            elif a == "보":
                                await message.channel.send(message.author.mention+", 봇: `보`, 당신: `가위` | 당신이 이겼습니다.")
                        elif c == "바위":
                            if a == "가위":
                                await message.channel.send(message.author.mention+", 봇: `가위`, 당신: `바위` | 당신이 이겼습니다.")
                            elif a == "바위":
                                await message.channel.send(message.author.mention+", 봇: `바위`, 당신: `바위` | 비겼습니다.")
                            elif a == "보":
                                await message.channel.send(message.author.mention+", 봇: `보`, 당신: `바위` | 당신이 졌습니다.")
                        elif c == "보":
                            if a == "가위":
                                await message.channel.send(message.author.mention+", 봇: `가위', 당신: `보` | 당신이 졌습니다.")
                            elif a == "바위":
                                await message.channel.send(message.author.mention+", 봇: `바위`, 당신: `보` | 당신이 이겼습니다.")
                            elif a == "보":
                                await message.channel.send(message.author.mention+", 봇: `보`, 당신: `보` | 비겼습니다.")
                    except:
                        await message.channel.send("어허... `가위`, `바위`, `보` 중 하나를 선택해줘! `예시) "+prefix+"가위바위보 가위`")

            if message.content == prefix+"도와줘" or message.content == prefix+"도움" or message.content == prefix+"help" or message.content == prefix+"헬프" or message.content == prefix+"헬프미" or message.content == prefix+"helpme" or message.content == prefix+"help me":
                await message.channel.send("도움 따윈 필요없다.")
                await message.channel.send("~~사실 아직 안만듬~~")
                log(prefix+"도와줘, "+prefix+"도움, "+prefix+"help, "+prefix+"헬프, "+prefix+"헬프미, "+prefix+"helpme, "+prefix+"help me", message.author, message.guild.name, message.guild.id, message.content)

            if message.content.startswith(prefix+"잠수"):
                if message.content[6:] == "":
                    await message.channel.send(message.author.mention+" 님이 잠수를 시작합니다.")
                    afklist.append(message.author.id)
                    log(prefix+"잠수", message.author, message.guild.name, message.guild.id, message.content)
                else:
                    reason = message.content[6:]
                    await message.channel.send(message.author.mention+" 님이 잠수를 시작합니다.\n사유: "+reason)
                    afklist.append(message.author.id)
                    log(prefix+"잠수", message.author, message.guild.name, message.guild.id, message.content)

            ##### 서버 관련 측정 
            if message.content == prefix+"핑": ## 내가 다시 생각해서 다시 만들자
                nowasdf = datetime.datetime.now()
                await message.channel.trigger_typing()
                latertime = datetime.datetime.now()            
                ping = latertime - nowasdf
                asdf = str(int(ping.microseconds) / 1000)
                asdf = asdf.split(".")
                asdf = asdf[0]
                await message.channel.send(message.author.mention+", %s ms" % asdf)
                log(prefix+"핑", message.author, message.guild.name, message.guild.id, message.content)

            if message.content == prefix+"온도":
                a = os.popen("vcgencmd measure_temp").read() # 라즈비안 or 라즈베리파이(ARM) 서버일경우 가능한 명령어.
                await message.channel.send("봇 <@%s> 서버의 온도는 현재 `%s` 이야!" % (str(476518072421711920), a))
                log(prefix+"핑", message.author, message.guild.name, message.guild.id, message.content)

            if message.content == prefix+"서버리스트" or message.content == prefix+"서리" or message.content == prefix+"serverlist":
                a = "" 
                user = 0 
                for s in client.guilds: 
                    a = a + "`" + s.name + "`" + "\n" 
                    user += s.member_count
                await message.channel.send("이 봇이 작동하는 서버는 `%s` 개 이고,\n모든서버의 유저수(중복)는 `%s` 명 이야!" % (str(len(client.guilds)), user))
                log(prefix+"서버리스트, "+prefix+"서리, "+prefix+"serverlist", message.author, message.guild.name, message.guild.id, message.content)

            if message.content == prefix+"서버리스트 자세히" or message.content == prefix+"서리 자세히" or message.content == prefix+"serverlist 자세히":
                a = "" 
                user = 0 
                for s in client.guilds: 
                    a = a + "`" + s.name + "`" + "\n" 
                    user += s.member_count
                embed=discord.Embed(title="", description=a)
                embed.set_footer(text="이 봇이 작동하는 서버는 `%s` 개 입니다.\n모든서버의 유저수(중복)는 `%s` 명 입니다." % (str(len(client.guilds)), user))
                await message.author.send(embed=embed)
                await message.channel.send("DM채널을 보시게 자네 "+message.author.mention)
                log(prefix+"서버리스트 자세히, "+prefix+"서리 자세히, "+prefix+"serverlist 자세히", message.author, message.guild.name, message.guild.id, message.content)

            if message.content == prefix+"업타임" or message.content == prefix+"켜진시간" or message.content == prefix+"온타임":
                uptime = datetime.datetime.now() - botstarttime
                day = uptime.days
                day = str(day)
                uptime = str(uptime)
                uptime = uptime.split(":")
                hours = uptime[0]
                hours = hours.replace(" days", "일")
                hours = hours.replace(" day", "일")
                minitues = uptime[1]
                seconds = uptime[2]
                seconds = seconds.split(".")
                seconds = seconds[0]

                await message.channel.send("현재 나는 `%s` 시간 `%s` 분 `%s` 초 동안 깨어있었어!" % (hours, minitues, seconds))

            ##### 관리자전용
            if message.content == prefix+"재시작":
                if str(message.author.id) == devid:
                    await client.change_presence(activity=discord.Game(name=restart_playing_msg))
                    await message.channel.send("재시작합니다...")
                    restart()
                    log(prefix+"재시작", message.author, message.guild.name, message.guild.id, message.content)
                else:
                    await message.channel.send("왜")
                    log(prefix+"재시작", message.author, message.guild.name, message.guild.id, message.content)
            if message.content == prefix+"종료":
                if str(message.author.id) == devid:
                    log(prefix+"종료", message.author, message.guild.name, message.guild.id, message.content)
                    await client.change_presence(activity=discord.Game(name=stop_playing_msg))
                    await message.channel.send("종료합니다... 이용해주셔서 감사합니다! ")
                    await client.close()
                else:
                    await message.channel.send("뭐")
                    log(prefix+"종료", message.author, message.guild.name, message.guild.id, message.content)

client = db()
client.run(token)
                
