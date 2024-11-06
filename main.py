from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


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
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

@dp.message(F.voice)
async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)

@dp.message()
async def send_echo(message: Message):
    ''' Этот хэндлер будет срабатывать на любые текстовые сообщения '''
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
