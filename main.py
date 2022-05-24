import os
import time
import asyncio
import telegram


async def main():
    while True:
        time.sleep(10)
        bot = telegram.Bot('5316370122:AAEwKTc3VvZPD1EBLzAtQ5gC9HO42YG0cFY')
        for address, dirs, files in os.walk('images'):
            for name in files:
                async with bot:
                    await bot.send_document(
                        chat_id=-1001633682543, 
                        document=open(os.path.join(address, name), 'rb')
                    )


if __name__ == '__main__':
    asyncio.run(main())
