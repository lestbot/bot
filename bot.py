import os
import time
import datetime
import json
import string
import discord
import random
import asyncio
import operator
from discord.ext import commands
from time import gmtime, strftime
import platform

startup_extensions = [""]
bot =commands.Bot(command_prefix="sv.")

     
###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
# ~ Informação do bot no log..
@bot.event
async def on_ready():
	print('Nome : '+bot.user.name)
	print('Id : '+bot.user.id)
	print('Servidores : '+str(len(bot.servers)))
	print('Usuários : '+str(len(set(bot.get_all_members())))+'')
	print('Discord.py Version: {} '.format(discord.__version__))
	print('Python Version : {} '.format(platform.python_version()))
	print("Convite : https://discordapp.com/oauth2/authorize?client_id="+bot.user.id+"&scope=bot&permissions=8")
#	return await bot.change_presence(game=discord.Game(name=' em  servidores')) 
	return await bot.change_presence(game=discord.Game(name="amor a "+str(len(bot.servers))+" Servidores", type=1, url='https://www.twitch.tv/nitrorocketleague'), status='Online') 

###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
# ~ Informação de quem entra no servidor.


###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
# ~ Informação das message no console (beta)
#https://pastebin.com/qYxb5T8W
@bot.event
async def on_message(message):
    rep = text = msg = message.content
    rep2 = text2 = msg2 = rep.split()
    user = str(message.author)
    try:
        server_msg = str(message.channel.server)
        chan_msg = str(message.channel.name)
        pm = False
    except AttributeError:
        server_msg = user
        chan_msg = user
        pm = True
    try:
        command = rep2[0].lower()
        params = rep2[0:]
    except IndexError:
        command = ""
        params = ""
    try:
      print("[Servidor] : "+server_msg+ " ("+chan_msg+") "+user+" - " + rep)
    except:
        print("[Servidor] : "+server_msg+ " ("+chan_msg+") "+user+" - erro")

    chan = message.channel
    con = message.content
    if con.startswith("<@403570895039496193>"):
       await bot.send_message(chan,"O quê foi?")
       joker.append(user)
    if con.startswith("nada não") or con.startswith("nada"):
     if user in joker:
        await bot.send_message(message.channel, "então porquê está me marcando?")
        joker.remove(user)
    elif con.lower().startswith("?emoji") and message.author.id in joker:
         await bot.send_message(chan, "<:check:314349398811475968>")

    elif con.lower().startswith("?eval") and message.author.id in joker:
        try:
            split = "================================"
            await bot.send_message(chan,content="```py\nInput: {0}\n{1}\n".format(message.content[6:] , split) + "Output: " + str(eval(message.content[6:])) + "```")
        except Exception as e:
            await bot.send_message(chan, "```py\n" + repr(e) + "```")

    if con.lower().startswith("?help"):
        if message.author.bot: return
        else:
            em = discord.Embed(description=None, colour=message.author.colour)
            em.add_field(name= "Administration:", value= "voicekick, role, purge, ban, kick, mute, unmute")
            em.add_field(name= "Fun:", value= "fancy, calculator, roll, suicide, mal, rps, illegal, rem, rolldice, 8ball, say")
            em.add_field(name= "Information:", value= "user, server, info, avatar, userid, remindme, serverinvite, nickname, invite")
            em.add_field(name= "Gambling:", value= "credits, flip, spin")
            em.set_footer(text="any errors with the bot, message Itz Splash#0012")
            await bot.send_message(message.channel, embed=em)
    await bot.process_commands(message)
    bot.remove_command("help")


###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
# ~ Informação de erro!
        

###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################################################################
# ~ Token para o bot ter acesso a sua conta

#bot.run("NDAzNTcwODk1MDM5NDk2MTkz.DUk-mg.p-su4NqJthRxAyzd_jGseH6AHhg")
bot.run("NDE1OTA3NDc5NjA0NDI4ODAw.DYzzdg.eKgXli3XKpBkKiAzmMkPkN8AlwI")
