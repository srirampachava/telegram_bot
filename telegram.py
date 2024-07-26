import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Use environment variable for the bot token
TOKEN = os.getenv("7338443707:AAHAXHp_k0nd7mOmflItrnXFS32x2lkq7HU")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to up bot now your a member of our channel and now type /help to get more options")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This particular message
        /content -> About various websites
        /anime -> To watch anime
        /movie -> To watch movies
        /series -> To watch series
        /contact -> Contact information
        """
    )
async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        We have various websites available for entertainment.
        /anime -> If you want to watch anime.
        /movie -> If you want to watch movies.
        /series -> If you want to watch series.
        /contact -> For Contact information.
        """
    )    


async def anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://animepahe.ru/")

async def movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://goku.sx/")

async def series(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://goku.sx/")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can contact the registered email provided on the website.")

# Create the application
application = ApplicationBuilder().token("7338443707:AAHAXHp_k0nd7mOmflItrnXFS32x2lkq7HU").build()

# Add command handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help_command))
application.add_handler(CommandHandler('content', content))
application.add_handler(CommandHandler('anime', anime))
application.add_handler(CommandHandler('movie', movie))
application.add_handler(CommandHandler('series', series))
application.add_handler(CommandHandler('contact', contact))

# Start the bot
application.run_polling()
