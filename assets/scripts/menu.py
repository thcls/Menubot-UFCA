from bs4 import BeautifulSoup
from requests import get
from json import dump
from assets.scripts.utils import menuToImage
#from utils import menuToImage

url = 'https://www.ufca.edu.br/assuntos-estudantis/refeitorio-universitario/cardapios/'

def setDate(date) -> None:
    with open('assets/json/date.json','w' ,encoding='utf-8') as json_file:
        dump(date, json_file)

async def getAttDate() -> dict:
    
    htmlString = get(url)
    html = BeautifulSoup(htmlString.content, "html.parser")
    div = html.find('div',"ui accordion")
    attDate = div.find_all('p').pop().text
    aList = div.find_all('a')
    menuNum = len(aList)
    
    title = div.find_all("div","content")
    title = title[-1].find('p').text
    
    title = title.replace('PRAE/RU/UFCA – ','')
    attDate = attDate.replace('Ultima atualização: ','')

    link = aList.pop().get('href')
    
    return { 
        'date': attDate,
        'length': menuNum,
        'title':title,
        'link': link
    }

async def getMenu() -> None:
    attDate = await getAttDate()
    
    menu = get(attDate["link"])
    
    with open("assets/menus/menu.pdf",'wb') as pdf:
        pdf.write(menu.content)
    
    menuToImage()
    
    setDate(attDate)

if __name__ == '__main__':
    getMenu()