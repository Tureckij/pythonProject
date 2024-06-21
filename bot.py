import telebot

# Инициализация бота с вашим токеном
bot = telebot.TeleBot('6606413665:AAFlfuSJ_HzD1aMyb0kLu1nT29ox85gh7jE')

# Обработчик сообщений с типом 'text'
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# Запуск бота
bot.polling(none_stop=True, interval=0)
