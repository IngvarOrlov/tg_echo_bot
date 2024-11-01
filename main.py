from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '6059463480:AAGGaRv1g_Cp1TolFz-023EQzX2sXvQauEQ'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    ''' Этот хэндлер будет срабатывать на команду "/start" '''
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    ''' Этот хэндлер будет срабатывать на команду "/help" '''
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


@dp.message()
async def send_echo(message: Message):
    ''' Этот хэндлер будет срабатывать на любые текстовые сообщения '''
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
