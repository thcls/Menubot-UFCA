import discord
from json import load
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from assets.scripts import menu
from assets.scripts import utils

test = False

if test == False:
    config = {
        "channelId": 1097001318821920858,
        "roleId": 957726404840153228,
        "logChannelId": 1124513287791448115,
        "menuInterval": 60 #segundoos
    }
else:
    config = {
        "channelId": 958543755613458462,
        "roleId": 957726404840153228,
        "logChannelId": 958543755613458462,
        "menuInterval": 0.2 #segundoos
    }

load_dotenv()

token = getenv("TOKEN")
run = [False]

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/',intents=intents)

async def running(config):
    try:
        dateAtt = await menu.getAttDate()
        logChannel = client.get_channel(config['logChannelId'])
        await logChannel.send(config["menuInterval"])
    except Exception as  error:
        logChannel = client.get_channel(config['logChannelId'])
        await logChannel.send(error)
        utils.timefunction(config)
        return
        
    with open('assets/json/date.json',encoding='utf-8') as json_file:
        date = load(json_file)
        
    if(dateAtt['date'] != date['date']):
        
        try:
            if(date['length']==dateAtt['length']):
                description = f'Hey <@&{str(config["roleId"])}>, o menu acaba de passar por uma atualização!'
            else:
                description = f'Hey <@&{str(config["roleId"])}>, {utils.randomLines()}'
                
            await menu.getMenu()
            
            channel = client.get_channel(config['channelId'])
            
            embed = discord.Embed(title=dateAtt['title'], description=description, color=0x0492EE)
            img =discord.File("assets/img/menuImg.png", filename="img.png")
            embed.set_image(url="attachment://img.png")
            embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
            embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2515/2515271.png')
            embed.set_footer(text="thcls", icon_url='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png')
            embed.add_field(name='PDF',value=f'[Link]({dateAtt["link"]})')
            embed.add_field(name='Data de atualização',value=dateAtt['date'])
            
            await channel.send(file=img,embed=embed)

        except Exception as error:
            logChannel = client.get_channel(config['logChannelId'])
            await logChannel.send(error)
            
    utils.timefunction(config)

@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print('We have logged')  
    except Exception as error:
        print(error)

@client.tree.command(name="startmenu")
async def startmenu(interaction: discord.Integration):
    if run[0] == True:
        await interaction.response.send_message('Outra instancia já esta rodando.')
        return
    else:
        run[0] = True
        await interaction.response.send_message('ok.')
    
    while run[0]:
        await running(config)
        await asyncio.sleep(config["menuInterval"])

@client.tree.command(name="stopmenu")
async def stopmenu(interaction: discord.Integration):
    run[0] = False
    try:
        await interaction.response.send_message('Ok, apartir de agora vou parar de enviar o menu.')
    except Exception as  error:
        print(error)
    
@client.tree.command(name="ping")
async def ping(interaction: discord.Integration):
    try:
        await interaction.response.send_message("Pong")
    except Exception as  error:
        print(error)

client.run(token)
