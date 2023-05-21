import discord
from json import load
import asyncio
from discord.ext import commands
from assets.scripts import menu
from assets.scripts import utils

test = False

token = utils.getToken()

if test == False:
    channelId = 1097001318821920858
    roleId = 957726404840153228
    logChannelId = 1096596708764418138
    menuInterval = 14400 #segundoos
    config = {
        "channelId": 1097001318821920858,
        "roleId": 957726404840153228,
        "logChannelId": 1096596708764418138,
        "menuInterval": 14400 #segundoos
    }
else:
    channelId = 1096596708764418138
    logChannelId = 1096596708764418138
    menuInterval = 10 #segundoos
    config = {
        "channelId": 1096596708764418138,
        "roleId": 957726404840153228,
        "logChannelId": 1096596708764418138,
        "menuInterval": 10 #segundoos
    }
    
run = [False]
botPrefix = '!'

intents = discord.Intents.all()
client = commands.Bot(command_prefix=botPrefix,intents=intents)

@client.event
async def on_ready():
    print('We have logged')        

@client.command()
async def startmenu(context):
    if run[0] == True:
        logChannel = client.get_channel(config['logChannelId'])
        await logChannel.send('Outra instancia já esta rodando.')
        return
    else:
        run[0] = True
        logChannel = client.get_channel(config['logChannelId'])
        await logChannel.send('ok.')
    
    while run[0]:
        try:
            dateAtt = menu.getAttDate()
        except Exception as  error:
            logChannel = client.get_channel(config['logChannelId'])
            await logChannel.send(error)
            
        with open('assets/json/date.json',encoding='utf-8') as json_file:
            date = load(json_file)
            
        if(dateAtt['date'] != date['date']):
            
            try:
                if(date['length']==dateAtt['length']):
                    description = 'Hey <@&{}>, o menu acaba de passar por uma atualização!'.format(str(config['roleId']))
                else:
                    description = 'Hey <@&{}>, {}'.format(str(config['roleId']),utils.randomLines())
                    
                menu.getMenu()
                
                channel = client.get_channel(config['channelId'])
                
                embed = discord.Embed(title=dateAtt['title'], description=description, color=0x0492EE)
                img =discord.File("assets/img/menuImg.png", filename="img.png")
                embed.set_image(url="attachment://img.png")
                embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
                embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2515/2515271.png')
                embed.set_footer(text="thcls", icon_url='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png')
                embed.add_field(name='PDF',value='[Link]({})'.format(dateAtt['link']))
                embed.add_field(name='Data de atualização',value=dateAtt['date'])
                
                await channel.send(file=img,embed=embed)
  
            except Exception as error:
                logChannel = client.get_channel(config['logChannelId'])
                await logChannel.send(error)
                
        await asyncio.sleep(menuInterval)

@client.command()
async def stopmenu(context):
    
    run[0] = False
    channel = client.get_channel(config['logChannelId'])
    try:
        await channel.send('Ok, apartir de agora vou parar de enviar o menu.')
    except Exception as  error:
        pass
    
@client.command()
async def ping(context):
    with open('assets/json/date.json',encoding='utf-8') as json_file:
            date = load(json_file)
    channel = client.get_channel(config['logChannelId'])
    try:
        await channel.send(date['date'])
    except Exception as  error:
        pass
    
client.run(token)
