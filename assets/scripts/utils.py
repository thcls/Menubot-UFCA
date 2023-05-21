from json import load, dump
import fitz
from random import randint

def menuToImage():
    with fitz.open('assets/menus/menu.pdf') as pdf:
        page = pdf[0]
        matrix = fitz.Matrix(5,5)
        img = page.get_pixmap(matrix=matrix,alpha=False).tobytes("png")
          
    with open('assets/img/menuImg.png', 'wb') as file:
        file.write(img)

def getToken():
    with open('assets/json/token.json',encoding='utf-8') as json_file:
        token = load(json_file)
    return token['token']

def randomLines():
    with open('assets/json/lines.json',encoding='utf-8') as json_file:
        lines = load(json_file)
    return lines[str(randint(1, 48))]

def saveChannelId(channelId, roleId):
    ids = {
        "channel": channelId,
        "role": roleId
    }
    
    channelsIds = getChannelids()
    channelsIds.append(ids)
    setChannelids(channelsIds)

def removeChannel(channelId):
    channelsIds = getChannelids()
    channelsQtd = len(channelsIds)
    for i in range(0, channelsQtd - 1):
        if channelsIds[i]['channel'] == channelId:
            channelsIds[i] = channelsIds.pop()
            return

def getChannelids():
    with open('assets/json/channels.json') as json_file:
        channelsIds = load(json_file)
    return channelsIds

def setChannelids(channelsIds):
    with open('assets/json/channels.json') as json_file:
        dump(channelsIds, json_file)
        
if __name__ == '__main__':
    menuToImage()