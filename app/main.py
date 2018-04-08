# coding=UTF-8
import telebot
from citgen import create_cit
import settings

bot = telebot.TeleBot(settings.token)

@bot.message_handler(commands=['citgen'])
def citgen(message):
    '''Цитген, он самый'''

    chat_id = message.chat.id


    trigger = False
    text = message.reply_to_message.text
    
    # Получает и сохраняет аватарку
    userpic = bot.get_user_profile_photos(message.reply_to_message.from_user.id)
    userpic_info = bot.get_file(userpic.photos[0][0].file_id)
    userpic_downloaded = bot.download_file(userpic_info.file_path)
    src = '../other/userpic.png' 
    with open(src, 'wb') as new_file:
        new_file.write(userpic_downloaded)
   
    # Получает юзернейм. Если его нет - использует имя.
    if message.reply_to_message.from_user.username != None:   
        username = '@' + message.reply_to_message.from_user.username  
        if message.reply_to_message.from_user.username == message.from_user.username:
            trigger = True   
    else:
        username = message.reply_to_message.from_user.first_name
        if message.reply_to_message.from_user.first_name == message.from_user.first_name:
            trigger = True

    citata = create_cit(text, username, trigger)

    print(citata)

    # Ограничение величины сообщения до 275 символов
    if len(text) > 275:
        bot.send_message(chat_id, u'Message is too large')  
    # Отправляет цитату. 
    else: 
        # в чат
        bot.send_photo(chat_id, 
                        open(citata, 'rb'), 
                        reply_to_message_id=message.reply_to_message.message_id)
        # в канал
        bot.send_photo(settings.channelusername, open(citata, 'rb'))

@bot.message_handler(commands=['gentoo'])
def gentoo_trigger(message):
    '''Выводит пасту про генту'''

    chat_id = message.chat.id

    f = open('../other/gentoo_compile.txt', 'r')
    text = '_' + f.read() + '_'
    f.close()
 
    bot.send_message(chat_id,          
                     text,
                     reply_to_message_id=message.message_id,
                     parse_mode='Markdown')

if __name__ == '__main__':
    bot.polling(none_stop=True)

