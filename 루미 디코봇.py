import discord
import requests
import asyncio
from json import loads
twitch_Client_ID = '4piqyxcimtq152kggv2b9kucazdq6w'
twitch_Client_secret = 'n8zita45ec6qmaxbdm35xn6l1kjb0y'
discord_Token = 'OTM3OTg0ODI5MTUxMTQxOTM4.Yfjscg.SnqRWq7BOoDEnKbecdd1hpTWHK8'
discord_channelID = 937347254837211187
discord_bot_state = '방송 알리미'
twitchID = 'sseung_23'
ment = '@everyone 방송 켰으니 놀러오세요오'
client = discord.Client()
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game(discord_bot_state)
    await client.change_presence(status=discord.Status.online, activity=game)
    channel = client.get_channel(discord_channelID)
    oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + twitch_Client_ID + "&client_secret=" + twitch_Client_secret + "&grant_type=client_credentials")
    access_token = loads(oauth_key.text)["access_token"]
    token_type = 'Bearer '
    authorization = token_type + access_token
    print(authorization)
    check = False  
    while True:
        print("ready on Notification")
        headers = {'client-id': twitch_Client_ID, 'Authorization': authorization}
        response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + twitchID, headers=headers)
        print(response_channel.text)
        try:
            if loads(response_channel.text)['data'][0]['type'] == 'live' and check == False:
                await channel.send(ment +'\n https://www.twitch.tv/' + twitchID)
                print("Online")
                check = True
        except:
            print("Offline")
            check = False
        await asyncio.sleep(30)
client.run(discord_Token)
