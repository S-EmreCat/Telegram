import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text("Commands: start-help-words-video-41days")

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('How can I help you!')

def todayvideo(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Video list: https://www.youtube.com/playlist?list=PLi35DK8T_m02xtqMe0EkucdUvdO6wjden')

#word list
def todaywords(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('@kelimeogren')   

def _41days(update,video):
    update.message.reply_text('https://www.youtube.com/playlist?list=PLi35DK8T_m03bnNmcVUk5sN8MXW-g__St')  


    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("video", todayvideo))
    dp.add_handler(CommandHandler("words", todaywords))
    dp.add_handler(CommandHandler("41days", _41days))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    


if __name__ == '__main__':
    main()


    