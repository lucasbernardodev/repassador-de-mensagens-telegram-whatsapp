import telegram

bot = telegram.Bot(token='SEU_TOKEN_TELEGRAM')

from telegram.ext import CommandHandler, MessageHandler, filters, Updater

# Função para repassar a mensagem do grupo X para o grupo Y
def repassar_mensagem_x_y(update, context):
    message = update.message.text
    print('Mensagem recebida:', message)  # adiciona essa linha
    try:
        context.bot.send_message(chat_id='ID_GRUPO_Y', text=message)
    except:
        context.bot.send_message(chat_id='ID_GRUPO_X', text="Não consegui ler a mensagem.")
    
    # Enviar mensagem
    context.bot.send_message(chat_id=update.message.chat_id, text=message)

# Configuração do bot do Telegram
updater = Updater(token='SEU_TOKEN_TELEGRAM', use_context=True)
dispatcher = updater.dispatcher

# Adiciona o handler para a função repassar_mensagem
#
dispatcher.add_handler(MessageHandler(filters.Filters.text & filters.Filters.chat(chat_id='-ID_GRUPO_X'), repassar_mensagem_x_y))

# Função para o comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu estou funcionando!")

# Adiciona o handler para o comando /start
dispatcher.add_handler(CommandHandler('start', start))

# Inicia o bot
updater.start_polling()
