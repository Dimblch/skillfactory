# SkillFactory QAP-89 задание 18.6.1
#
# Ваше задание: написать и протестировать Telegram-бота

import telebot
from config import keys, TOKEN
from extensions import APIException, Convert


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Для начала работы введите команду в следующем формате:\n \
<валюта которая у вас есть> <валюта на которую хотите обменять> <количество>\n \
Например: доллар рубль 10\n \
Список доступных для расчёта валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Неверное количество параметров, подробнее в /help')

        base, quote, amount = values
        total = Convert.get_price(base, quote, amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду:\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} = {total}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)