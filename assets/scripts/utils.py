from json import load, dump
import fitz
from random import randint

def menuToImage() -> None:
    with fitz.open('assets/menus/menu.pdf') as pdf:
        page = pdf[0]
        matrix = fitz.Matrix(4,4)
        img = page.get_pixmap(matrix=matrix,alpha=False).tobytes("png")
          
    with open('assets/img/menuImg.png', 'wb') as file:
        file.write(img)

def randomLines() -> str:
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

def timefunction(config) -> None:
    if config["menuInterval"] >= 7200:
        config["menuInterval"] = 60
    else:
        config["menuInterval"] *= 2
if __name__ == '__main__':
    menuToImage()