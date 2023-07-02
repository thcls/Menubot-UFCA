import discord
from json import load
from asyncio import sleep
from discord.ext import commands, tasks
from dotenv import load_dotenv
from os import getenv
from assets.scripts import menu
from assets.scripts import utils

test = True
config = utils.getConfig(test)

load_dotenv()
token = getenv("TOKEN")

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)

async def getEmbed(date, dateAtt) -> discord.Embed:
    if(date['length']==dateAtt['length']):
        description = f'Hey <@&{str(config["roleId"])}>, o menu acaba de passar por uma atualização!'
    else:
        description = f'Hey <@&{str(config["roleId"])}>, {utils.randomLines()}'
    
    embed = discord.Embed(title=dateAtt['title'], description=description, color=0x0492EE)
    embed.set_image(url="attachment://img.png")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
    embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2515/2515271.png')
    embed.set_footer(text="thcls", icon_url='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png')
    embed.add_field(name='PDF',value=f'[Link]({dateAtt["link"]})')
    embed.add_field(name='Data de atualização',value=dateAtt['date'])
    
    return embed

async def running(config) -> None:
    logChannel = client.get_channel(config['logChannelId'])
    
    try:
        dateAtt = await menu.getAttDate()

        await logChannel.send(config["menuInterval"])
    
        
        with open('assets/json/date.json',encoding='utf-8') as json_file:
            date = load(json_file)
            
        if(dateAtt['date'] != date['date']):   
            await menu.getMenu()
            
            img =discord.File("assets/img/menuImg.png", filename="img.png")
            embed = await getEmbed(date, dateAtt)
            
            channel = client.get_channel(config['channelId'])
            await channel.send(file=img,embed=embed)

    except Exception as  error:
        await logChannel.send(error)
            
@client.event
async def on_ready() -> None:
    try:
        synced = await client.tree.sync()
        print('We have logged')  
    except Exception as error:
        print(error)

@client.tree.command(name="startmenu")
async def startmenu(interaction: discord.Integration) -> None:
    if config["run"] == True:
        await interaction.response.send_message('Outra instancia já esta rodando.')
        return
    else:
        config["run"] = True
        await interaction.response.send_message('ok.')
    
    while config["run"]:
        await running(config)
        await sleep(config["menuInterval"])
        utils.timefunction(config)

@client.tree.command(name="stopmenu")
async def stopmenu(interaction: discord.Integration) -> None:
    config["run"] = False
    try:
        await interaction.response.send_message('Ok, apartir de agora vou parar de enviar o menu.')
    except Exception as  error:
        print(error)
    
@client.tree.command(name="ping")
async def ping(interaction: discord.Integration) -> None:
    try:
        await interaction.response.send_message("Pong")
    except Exception as  error:
        print(error)

client.run(token)