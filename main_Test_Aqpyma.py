from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
    CallbackContext,
)


VENTAS = 0,
INSIGHTS = 0,
END = 0,


def start(update:Update, context: CallbackContext) -> str: 
    text = ("Por favor, escoge una de las funciones que están en los botones a continuación")

    buttons = [
        [ 
            InlineKeyboardButton(text = 'Ventas',callback_data = str(VENTAS)),
            InlineKeyboardButton(text = 'Insights', callback_data = str(INSIGHTS)),
            InlineKeyboardButton(text = 'Terminar Sesión', callback_data = str(END)),
        ]   
    ]
    keyboard = InlineKeyboardMarkup(buttons)


    update.message.reply_text(text = text, reply_markup = keyboard)
with open('token.txt','r') as f:
    TOKEN = f.read()

if __name__ == '__main__':
    updater = Updater(token = TOKEN, use_context=True)

#se encarga de enviar las acciones
    dp = updater.dispatcher

#Vinculamos el handler con el dispatcher, creado un comando handler start, cuando entre ese comando, se ejecuta la función start
    dp. add_handler(CommandHandler('start', start))

#Crea un ciclo para ver si el usuario manda 1 mensaje 
    updater.start_polling()
    updater.idle()
