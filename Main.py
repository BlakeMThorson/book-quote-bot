
import discord
import asyncio
from discord.utils import find
import helper1
from helper1 import *
client=discord.Client()





@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

    
@client.event
async def on_message(message):
    
    
  
    if message.content.startswith("(debug 124)"):
        x = message.content.replace("(debug 124)","")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(x))
    
    
    elif message.content == "<@592451535099920386>":
        name = "**{}**".format(message.mentions[0].name)
        command1 = "**~Quote (Author)**"
        Helpmessage = """
        **Thanks for adding me to {}**!
        
        ***Description***
        I am able to give you a random quote from your favorite author. I use GoodReads as a source, so not all quotes maybe in your language.
        
        ***Commands***
        {}
        
        ***Support The Creator***
                Please support the creator by sharing me to other servers using the following link: 
https://discordapp.com/api/oauth2/authorize?client_id=592451535099920386&permissions=0&scope=bot
        or through the following links.
        -<:patreon:630306170791395348> https://www.patreon.com/b9king
        -<:paypal:630306883105849354> https://www.paypal.com/paypalme2/b9king
        Or you can visit him here: https://benignking.xyz :heart:
        """.format(message.guild.name,command1)
        
        embed=discord.Embed(title="", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url= message.mentions[0].avatar_url)
        await message.channel.send(embed=embed)   
        
        
    
    
    if message.content.startswith("~Quote"):
        
        g = message.content.replace("~Quote ","")
        z = Quote(g)
        embed=discord.Embed(title="Quote From {}".format(z[1]), description="{}".format(z[0][:500]), color=0xff8080)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/72/google/6/books_1f4da.png")
        await message.channel.send(embed=embed)       
    



                
                
client.run('NTkyNDUxNTM1MDk5OTIwMzg2.XRWsog.H1kOKvjT62C6kWwa7h8zoJBD-g8') 

