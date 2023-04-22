from json import load
import fitz
from random import randint

def menuToImage():
    with fitz.open('assets/menus/menu.pdf') as pdf:
        page = pdf[0]
        matrix = fitz.Matrix(5,5)
        img = page.get_pixmap(matrix=matrix,alpha=False).tobytes("png")
          
    with open('assets/menus/menuImg.png', 'wb') as file:
        file.write(img)

def getToken():
    with open('assets/json/token.json',encoding='utf-8') as json_file:
        token = load(json_file)
    return token['token']

def randomLines():
    with open('assets/json/lines.json',encoding='utf-8') as json_file:
        lines = load(json_file)
    return lines[str(randint(1, 48))]

if __name__ == '__main__':
    menuToImage()