from telebot import TeleBot, types
import time


TOKEN = '7057302012:AAELgvrojjWbbglPEA1aylrHIUHSRKYYoEM'
bot = TeleBot(TOKEN)

with open('b_words.txt', 'r', encoding = 'UTF-8') as words:
    b_words = []
    for word in words.readlines():
        b_words.append(word.strip().lower())
    print(b_words)

ban_time = 20 # seconds

def check_b_words(text):
    is_bun = False
    user_words = text.split(' ')
    for word in user_words:
        if word.lower() in b_words: is_bun = True
    return is_bun 

@bot.message_handler()
def get_message(message):
    is_bun = check_b_words(message.text)
    print(is_bun)
    if is_bun:
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        send_text = first_name + ' ' + last_name + ' ЗАБАНЕН на ' + str(ban_time) + ' секунд!'
        bot.send_message(message.chat.id, text=send_text, reply_to_message_id=message.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time.time()+ban_time)
    else:
        bot.send_message(message.chat.id, text = 'OK')


if __name__ == '__main__':
    bot.polling(non_stop=True)