from telebot import TeleBot
from telebot.types import Message


bot = TeleBot('7698466846:AAEtkZ2OLKq-ElmaurZ2UsW33_f_TxbvtqY')
admin = '@ahmadjonovazizbek'
group_id = '-1002297206867'


@bot.message_handler(commands=['start', 'help', 'dev', 'id'], chat_types=['private'])
def reaction_to_start(message: Message):
    print(message.chat)
    print(message)
    chat_id = message.chat.id
    if message.text == '/help':
        bot.send_message(chat_id, "Ushbu @first_fn27_bot Na'jot Ta'lim o'quvchisi Azizbek Ahmadjonov tomonidan "
                                  "2024-yilning 11-oktabr kuni yaratildi!")
    elif message.text == '/start':
        bot.send_message(chat_id, f"Assalomu alaykum {message.from_user.full_name}")
        bot.send_message(chat_id, "Bot haqida ma'lumot olish uchun /help buyrug'ini kiriting!")
    elif message.text == '/dev':
        bot.send_message(chat_id, f"Admin: {admin}")
    elif message.text == '/id':
        bot.send_message(chat_id, f"Sizning id: {message.from_user.id}")


@bot.message_handler(content_types=['animation', 'text', 'photo', 'video', 'document', 'sticker'], chat_types=['private'])
def reactio_to_content(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    user_text = f"👤 {full_name} dan xabar:\n\n"
    bot.send_message(group_id, user_text)
    bot.copy_message(group_id, chat_id, message.message_id)


bot.infinity_polling()
