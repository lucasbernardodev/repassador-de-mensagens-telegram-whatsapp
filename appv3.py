import telegram
from selenium import webdriver
import time

bot = telegram.Bot(token='SEU_TOKEN_TELEGRAM')

# Declaração da variável para armazenar a mensagem encaminhada para o grupo do WhatsApp
msgToWhats = ""

def repassar_mensagem(update, context):
    message = update.message.text
    bot.send_message(chat_id='ID_GRUPO_Y', text=message)
    # bot.send_message(chat_id='ID_DO_GRUPO_Z', text=message)

    # Atribui a mensagem para a variável 'msgToWhats'
    global msgToWhats
    msgToWhats = message

# Configuração do bot do Telegram
from telegram.ext import Updater, MessageHandler, filters

updater = Updater(token='SEU_TOKEN_TELEGRAM', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(filters.Chat(chat_id='ID_GRUPO_X'), repassar_mensagem))

updater.start_polling()

# A variável 'msgToWhats' estará disponível aqui após a mensagem ter sido encaminhada
# Ela contém a última mensagem encaminhada pelo bot para os grupos Y e Z
# A variável 'msgToWhats' está localizada fora da função 'repassar_mensagem', no escopo global do programa
    
# Loop para enviar a mensagem para o WhatsApp Web
while True:
    # Abre o navegador e acessa a página do WhatsApp Web
    driver = webdriver.Chrome('/webdriver/chromedriver')
    driver.get('https://web.whatsapp.com/')

    # Espera o usuário fazer o login no WhatsApp Web
    input('Faça o login no WhatsApp Web e pressione Enter para continuar...')

    # Define a mensagem que será enviada
    mensagem = msgToWhats

    # Busca o campo de pesquisa e envia a mensagem para o contato/grupo
    campo_pesquisa = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    campo_pesquisa.send_keys('Nome do contato/grupo')
    campo_pesquisa.submit()
    time.sleep(3)  # Aguarda o WhatsApp carregar a conversa

    campo_mensagem = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"][@spellcheck="true"]')
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.submit()

    # Fecha o navegador
    driver.quit()

    # Aguarda 5 minutos antes de enviar a próxima mensagem
    time.sleep(300)