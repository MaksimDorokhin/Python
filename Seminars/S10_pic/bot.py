import asyncio

from aiogram import Bot, Dispatcher, executor, filters, types
from pathlib import Path

API_TOKEN = '5572256145:AAGRs0BU9FnZVzZpgmtCJo7tMGus7mN1Nm0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(filters.CommandStart())
async def send_welcome(message: types.Message):
    # So... At first I want to send something like this:
    await message.reply("Здарова, что ты тут забыл?")

    # Wait a little...
    await asyncio.sleep(1)

    # Good bots should send chat actions...
    await types.ChatActions.upload_photo()

    # Create media group
    media = types.MediaGroup()

    path = Path.home() /'Downloads' / 'whale.jpeg'
    # Attach local file
    media.attach_photo(types.InputFile(path), 'Whale!')
    # More local files and more cats!
    # media.attach_photo(types.InputFile('data/cats.jpg'), 'More cats!')

    # You can also use URL's
    # For example: get random puss:
    media.attach_photo('http://lorempixel.com/400/200/cats/', 'Random cat.')

    # And you can also use file ID:
    # media.attach_photo('<file_id>', 'cat-cat-cat.')

    # Done! Send media group
    await message.reply_media_group(media=media)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)