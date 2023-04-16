from assets.scripts import bot
from assets.scripts import menu
import asyncio
from json import load

async def main():
    while True:
        try:
            dateAtt = menu.getAttDate()
        except Exception as  error:
            print(error)
        with open('assets/json/date.json',encoding='utf-8') as json_file:
            date = load(json_file)
        if(dateAtt['date'] != date['date']):
            try:
                menu.getMenu()
                if(dateAtt['length']==dateAtt['length']):
                    newMenu = False
                else:
                    newMenu = True
                await bot.main(newMenu)
            except Exception as error:
                print(error)
        print('4 horas se passaram.')
        await asyncio.sleep(14400)

asyncio.run(main())