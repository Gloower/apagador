from colorama import Fore, Back, Style, init
from os import system
import shutil
import subprocess
import discord
#/////////////////////////////////////////////////////
client = discord.Client()
token = ""

def champagne(cmd):
    subprocess.call(cmd, shell=True)
#/////////////////////////////////////////////////////

@client.event


async def on_ready():
    system("title Apagador - Feito por: Gloower")

    width = shutil.get_terminal_size().columns
    cpink = Style.DIM + Fore.CYAN
    
    
    def ui(): 
        champagne('cls')
        print("\n\n")
        print(cpink + """                                           ______                              
                                          / ____| |                             
                                         | |  __| | ___   _____      _____ _ __ 
                                         | | |_ | |/ _ \ / _ \ \ /\ / / _ \ '__|
                                         | |__| | | (_) | (_) \ V  V /  __/ |   
                                          \_____|_|\___/ \___/ \_/\_/ \___|_|   
                                        
  """)
        print(cpink + "[-] Desenvolvido por Gloower’ [-]".center(width))
        print(cpink + "[-] Usuário: {0} [-]".format(client.user).center(width))
        print(cpink + "[Bem vindo] Pronto! Estou aguardando o seu comando...".center(width)) 
        print(cpink + "Utilize o comando Limpar no chat desejado.".center(width)) 
        print("\n\n")
    ui()
 
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel
        
        width = shutil.get_terminal_size().columns
        cpink = Style.BRIGHT + Fore.MAGENTA

        if commands[0] == 'limpar':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == 'clear':
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                        except:
                             pass

                    
client.run(token, bot=False)
