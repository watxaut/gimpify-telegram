import logging

import gimpify
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

from config import FACE_IMAGE_PATH, JSON_FACES_PATH, BACKGROUND_IMAGE_PATH, JSON_BACKGROUNDS_PATH
from src.bot import start, montage, input_received
from src.secret import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':

    logger.info('--- Creating json file for faces ---')
    gimpify.create_face_json(FACE_IMAGE_PATH, JSON_FACES_PATH)

    logger.info('--- Creating json file for backgrounds ---')
    gimpify.create_background_json(BACKGROUND_IMAGE_PATH, JSON_BACKGROUNDS_PATH)

    # telegram bot init
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # adds the functions to the bot
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('tothemoon', montage))
    dispatcher.add_handler(CommandHandler('onlyfacepls', montage))
    dispatcher.add_handler(MessageHandler(filters.Filters.photo, input_received))
    dispatcher.add_handler(MessageHandler(filters.Filters.text, input_received))

    logger.info('--- Starting bot ---')

    # starts receiving calls
    updater.start_polling(timeout=10)
    updater.idle()
