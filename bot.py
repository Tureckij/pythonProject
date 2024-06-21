import telepot
from telepot.loop import MessageLoop

# Ваш токен, полученный от BotFather
TOKEN = '6606413665:AAFlfuSJ_HzD1aMyb0kLu1nT29ox85gh7jE'


# Функция-обработчик сообщений
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']

        if command == '/start':
            bot.sendMessage(chat_id, "Привет! Я бот. Чем могу помочь?")
        elif command == '/help':
            bot.sendMessage(chat_id, "Список доступных команд:\n/start - Начать общение\n/help - Получить помощь")
        else:
            bot.sendMessage(chat_id, "Извините, я не понимаю эту команду.")


# Инициализация бота
bot = telepot.Bot(TOKEN)


# Начало прослушивания сообщений
MessageLoop(bot, handle).run_as_thread()

print('Бот запущен и готов к работе.')

# Бот будет работать до тех пор, пока не остановить программу
import time

while True:
    time.sleep(10)
