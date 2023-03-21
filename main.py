'''
import asyncio
import json

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked
import logging
from os import getenv
from sys import exit

logging.basicConfig(level = logging.INFO)



bot = Bot(token = '6294178513:AAGSOAb1P2_8P6EL4u-WEtHjq97tTMoF6_k')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    await message.answer('You have typed /start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)


'''





'''

@dp.message_handler(commands='answer')
async def ans_m(message: types.Message):
    await message.answer('SMTHT')

@dp.message_handler(commands='reply')
async def rep_m(message: types.Message):
    await message.reply('SMTHT')

@dp.message_handler(commands='dice')
async def echo_message(message: types.Message):
    await message.answer_dice(emoji='🎲')

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Hello! write something")

@dp.message_handler(commands=['help'])
async def help_func(message: types.Message):
    await message.reply('write something and I will send it back')

@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
'''
'''
inline keyboard markup
inline keyboard button

'''



'''

import requests
prefix = 'https://api.telegram.org/bot'
geturl = prefix + bot_token + '/getUpdates'
sendurl = prefix + bot_token + '/sendMessage'
timeout = 40


def main():
    offset = 0
    while True:
        dt = dict(offset = offset, timeout = timeout)
        try:
            req = requests.post(geturl, data = dt, timeout=None).json()
        except ValueError:
            continue
        if not req['ok'] or not req['result']:
            continue
        for r in req['result']:
                message = r['message']
                id = message['chat']['id']
                if 'text' in message:
                    dt = dict(chat_id = id, text = 'reply')
                    requests.post(sendurl, data= dt).json()
                offset = r['update_id'] + 1
                if 'text' in message:
                    keyboard = json.dumps({'inline_keyboard':[[{'text':'YES', 'callback_data': '1'}, {'text':'NO', 'callback_data': '2'}]]})
                    dt = dict(chat_id = id, text = 'relpy', reply_markup = keyboard)
                    print(requests.post(sendurl, data = dt).json())

main()

'''







'''
import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_TOKEN = 'Ваш  токен'

# webhook settings
WEBHOOK_HOST = 'адрес сайта'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 3001

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dp):
   await bot.set_webhook(WEBHOOK_URL)
   # insert code here to run it after start


async def on_shutdown(dp):
   logging.warning('Shutting down..')

   # insert code here to run it before shutdown

   # Remove webhook (not acceptable in some cases)
   await bot.delete_webhook()

   # Close DB connection (if used)
   await dp.storage.close()
   await dp.storage.wait_closed()

   logging.warning('Bye!')


if __name__ == '__main__':
   start_webhook(
       dispatcher=dp,
       webhook_path=WEBHOOK_PATH,
       on_startup=on_startup,
       on_shutdown=on_shutdown,
       skip_updates=True,
       host=WEBAPP_HOST,
       port=WEBAPP_PORT,
   )


'''








'''
import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


API_TOKEN = '6294178513:AAGSOAb1P2_8P6EL4u-WEtHjq97tTMoF6_k'

WEBHOOK_HOST = 'https://7b8c-2a00-1370-81ae-1650-10a-65e6-6eea-67d.eu.ngrok.io'
WEBHOOK_PATH = ''
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = 3001


logging.basicConfig(level = logging.INFO)

bot = Bot(API_TOKEN)

dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    logging.warning('Shutting down...')
    await bot.delete_webhook()
    logging.warning('Bye!')

@dp.message_handler(commands = ['start'])
async def start_func(message: types.Message):
    return SendMessage(message.chat.id, message.text)

@dp.message_handler(commands = ['help'])
async def help_func(message: types.Message):
    return SendMessage(message.chat.id, 'I am helper func')

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup = on_startup,
        on_shutdown = on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
'''





import logging

from aiogram import Bot, types, Dispatcher, executor

API_TOKEN = '6294178513:AAGSOAb1P2_8P6EL4u-WEtHjq97tTMoF6_k'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    await message.reply('Start')


@dp.message_handler(commands=['help'])
async def help_func(message: types.Message):
    await message.reply('Help')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



























