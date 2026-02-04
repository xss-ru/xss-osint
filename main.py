import telebot
from telebot import types

bot = telebot.TeleBot("8411960026:AAH9JhT-8IwpYHox4GX0RBV6ODGfHg4fIt8")
OWNER_ID = 87560475

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        video = open('onion.mp4', 'rb')
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton("🔍OSINT", callback_data='osint')
        btn2 = types.InlineKeyboardButton("🛢DataBase", callback_data='database')
        btn3 = types.InlineKeyboardButton("🌐Web-Chat", callback_data='webchat')
        btn4 = types.InlineKeyboardButton("🧧Profile", callback_data='profile')
        btn5 = types.InlineKeyboardButton("💳Buy sub", callback_data='buysub')
        btn6 = types.InlineKeyboardButton("🎫Owner", callback_data='owner')
        markup.add(btn1, btn2, btn3)
        markup.add(btn4, btn5, btn6)
        if message.from_user.id == OWNER_ID:
            btn7 = types.InlineKeyboardButton("💻Admin - Panel", callback_data='admin')
            markup.add(btn7)
        caption = "<b>xss - osint: информационный агрегатор. Базы: 10 ТБ (публичные данные) + 17 ТБ (закрытые источники), Google dorking.\nИспользование - исключительно в исследовательских целях. Ответственность лежит на пользователе.</b>"
        bot.send_video(message.chat.id, video, caption=caption, parse_mode='HTML', reply_markup=markup)
        video.close()
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == "osint":
            bot.answer_callback_query(call.id, "OSINT")
        elif call.data == "database":
            bot.answer_callback_query(call.id, "DataBase")
        elif call.data == "webchat":
            bot.answer_callback_query(call.id, "Web-Chat")
        elif call.data == "profile":
            bot.answer_callback_query(call.id, "Profile")
        elif call.data == "buysub":
            bot.answer_callback_query(call.id, "Buy sub")
        elif call.data == "owner":
            bot.answer_callback_query(call.id, "Owner")
        elif call.data == "admin":
            bot.answer_callback_query(call.id, "Admin - Panel")
    except Exception as e:
        bot.answer_callback_query(call.id, f"Error: {str(e)}")

if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=60)
