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

def saveChannelId(channelId, roleId) -> None:
    ids = {
        "channel": channelId,
        "role": roleId
    }
    
    channelsIds = getChannelids()
    channelsIds.append(ids)
    setChannelids(channelsIds)

def removeChannel(channelId) -> None:
    channelsIds = getChannelids()
    channelsQtd = len(channelsIds)
    for i in range(0, channelsQtd - 1):
        if channelsIds[i]['channel'] == channelId:
            channelsIds[i] = channelsIds.pop()
            return

def getChannelids() -> list:
    with open('assets/json/channels.json') as json_file:
        channelsIds = load(json_file)
    return channelsIds

def setChannelids(channelsIds) -> None:
    with open('assets/json/channels.json') as json_file:
        dump(channelsIds, json_file)

def timefunction(config) -> None:
    if config["menuInterval"] >= 7200:
        config["menuInterval"] = 60
    else:
        config["menuInterval"] *= 2

def getConfig(test) -> dict:
    if test == False:
        config = {
            "channelId": 1097001318821920858,
            "roleId": 957726404840153228,
            "logChannelId": 1124513287791448115,
            "mainChannelId": 1125280022110933024,
            "menuInterval": 60, #segundoos
            "run": False
        }
    else:
        config = {
            "channelId": 958543755613458462,
            "roleId": 957726404840153228,
            "logChannelId": 958543755613458462,
            "menuInterval": 0.2, #segundoos
            "mainChannelId":1125280022110933024,
            "run": False
        }
    return config

if __name__ == '__main__':
    menuToImage()