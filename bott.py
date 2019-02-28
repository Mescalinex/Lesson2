from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, ephem, datetime
import sett

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[logging.FileHandler('bott.log', 'w', 'utf-8')]
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

mer = ephem.Mercury(datetime.date.today())
ven = ephem.Venus(datetime.date.today())
mar = ephem.Mars(datetime.date.today())
jup = ephem.Jupiter(datetime.date.today())
sat = ephem.Saturn(datetime.date.today())
ura = ephem.Uranus(datetime.date.today())
nep = ephem.Neptune(datetime.date.today())
plu = ephem.Pluto(datetime.date.today())

def greet_user(bot, update):
    logging.info('Вызван /start')
    update.message.reply_text('Добро пожаловать!')

def planets(bot, update):
    logging.info('Вызван /planet')
    update.message.reply_text('Введите название планеты:')
    
def talk_to_me(bot, update):
    user_text = update.message.text
    if user_text == 'Mercury':
        update.message.reply_text(ephem.constellation(mer))
    elif user_text == 'Venus':
        update.message.reply_text(ephem.constellation(ven))
    elif user_text == 'Mars':
        update.message.reply_text(ephem.constellation(mar))
    elif user_text == 'Jupiter':
        update.message.reply_text(ephem.constellation(jup))
    elif user_text == 'Saturn':
        update.message.reply_text(ephem.constellation(sat))
    elif user_text == 'Uranus':
        update.message.reply_text(ephem.constellation(ura))
    elif user_text == 'Neptune':
        update.message.reply_text(ephem.constellation(nep))
    elif user_text == 'Pluto':
        update.message.reply_text(ephem.constellation(plu))

    logging.info('User: %s, Chat id: %s, Message^ %s', update.message.chat.username, update.message.chat.id, update.message.text)

def main():
    mybot = Updater(sett.SECRET_BOT_KEY, request_kwargs=PROXY)
    
    logging.info('Бот запускается') 

    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) 
    
    mybot.start_polling()  
    mybot.idle() 

main()
