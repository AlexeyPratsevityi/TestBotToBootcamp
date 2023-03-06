import os
import logging
import time
from aiogram import Bot, types, executor, Dispatcher


TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Здравствуйте! Я помогу вам написать ФИО на латинице в соответствии'
                                                 ' с Приказом МИД России от 12.02.2020 № 2113')
    await message.answer('Напишите ФИО на кирилице')
    # logging.basicConfig(level='INFO', filename='my_log.log', format="%(asctime)s %(levelname)s %(message)s")
    logging.basicConfig(level='INFO', format="%(asctime)s %(levelname)s %(message)s")
    logging.info(f'user_id = {message.from_user.id} full_name = {message.from_user.full_name} text = {message.text}')

@dp.message_handler()
async def translit(message: types.Message):
    translit_dict = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH',
        'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Ъ': 'IE', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA'}
    new_d = {}
    for key, value in translit_dict.items():
        new_key = key.lower()
        new_value = value.lower()
        new_d[new_key] = new_value
    translit_dict.update(new_d)
    translit_text = ''
    for char in message.text:
        if char in translit_dict:
            translit_text += translit_dict[char]
        else:
            translit_text += char
    await message.answer(translit_text)
    full_name = message.from_user.full_name
    logging.info(f'user_id = {message.from_user.id} full_name = {message.from_user.full_name} text = {message.text}, answer = {translit_text}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)