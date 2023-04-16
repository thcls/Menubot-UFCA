import discord
from json import load
from random import randint
import asyncio

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def getToken():
    with open('assets/json/token.json',encoding='utf-8') as json_file:
        token = load(json_file)
    return token['token']

token = getToken()  

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
async def sendMessage(newMenu, client):
    await client.wait_until_ready()
    channel = client.get_channel(1097001318821920858)
    with open('assets/json/lines.json',encoding='utf-8') as json_file:
        lines = load(json_file)
        file = discord.File('assets/menus/menu.pdf')
        if not newMenu:
            await channel.send('Hey <@&957726404840153228>, ' + 'o menu acaba de passar por uma atualização!')
        else:
            await channel.send('Hey <@&957726404840153228>, ' + lines[str(randint(1, 48))])
        
        await channel.send(file=file)
        print('Arquivo enviado')
    await client.close()

async def main(newMenu):
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    await asyncio.gather(client.start(token),sendMessage(newMenu, client))

if __name__ == '__main__':
    asyncio.run(main(True))