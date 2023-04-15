from bs4 import BeautifulSoup
import requests
from json import dump

def updateDate(attDate, menuNum):
    date = { 'date': attDate,
            'length': menuNum
            }
    with open('assets/json/date.json','w' ,encoding='utf-8') as json_file:
        dump(date, json_file)

def getAttDate():
    url = 'https://www.ufca.edu.br/assuntos-estudantis/refeitorio-universitario/cardapios/'
    
    htmlString = requests.get(url)
    html = BeautifulSoup(htmlString.content, "html.parser")
    div = html.find('div',"ui accordion")
    attDate = div.find_all('p').pop().text
    aList = div.find_all('a')
    menuNum = len(aList)
    
    date = { 
        'date': attDate,
        'length': menuNum
        }
    return date
    
def getMenu():
    url = 'https://www.ufca.edu.br/assuntos-estudantis/refeitorio-universitario/cardapios/'
    
    htmlString = requests.get(url)
    html = BeautifulSoup(htmlString.content, "html.parser")
    div = html.find('div',"ui accordion")
    attDate = div.find_all('p').pop().text
    aList = div.find_all('a')
    
    menus = []
    
    for a in aList:
        menus.append(a.get('href'))
    menu = requests.get(menus.pop())
    
    with open("assets/menus/menu.pdf",'wb',encoding='utf-8') as pdf:
         pdf.write(menu.content)

    updateDate(attDate, len(aList))
def main():
    getMenu()


if __name__ == '__main__':
    main()