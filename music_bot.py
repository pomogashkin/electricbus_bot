import logging
import os

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([
        ['акустика', 'жизнь это как... эммм...'],
        ['мерзкий мир вымышленной реальности']
    ], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='привет, {}. что хочешь послушать?'.format(name),
        reply_markup=button
    )


def what(update, context):
    chat = update.effective_chat
    id = chat.id
    text = update.message.text
    if text == 'жизнь это как... эммм...':
        context.bot.send_photo(chat.id, open('img/live.jpeg', 'rb+'))
        for music in os.listdir('music/singls'):
            context.bot.send_audio(id, open('music/singls/' + music, 'rb+'))
    elif text == 'акустика':
        context.bot.send_photo(id, open('img/home.JPG', 'rb+'))
        for music in os.listdir('music/home'):
            context.bot.send_audio(id, open('music/home/' + music, 'rb+'))
    elif text == 'мерзкий мир вымышленной реальности':
        context.bot.send_photo(id, open('img/worst_img.jpg', 'rb+'))
        for music in os.listdir('music/worst_world'):
            context.bot.send_audio(id, open(
                'music/worst_world/' + music, 'rb+'
            ))
    else:
        context.bot.send_message(id, 'я нихуя не понял, че ты сказал, братан')


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, what))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
