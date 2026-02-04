import telebot
from telebot import types
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

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
        logger.info(f"User {message.from_user.id} started bot")
    except Exception as e:
        logger.error(f"Error in send_welcome: {str(e)}", exc_info=True)
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == "osint":
            bot.answer_callback_query(call.id, "OSINT")
            logger.info(f"User {call.from_user.id} clicked OSINT")
        elif call.data == "database":
            database_text = """<b>Базы данных находящиеся на наших серверах</b>

<b>Сбербанк (клиенты):</b> <code>~200 млн.</code>
<b>DNS-shop:</b> <code>11 млн.</code>
<b>2ГИС (сотрудники):</b> <code>225 тыс.</code>
<b>HeadHunter (hh.ru):</b> <code>40 млн.</code>
<b>МТС (клиенты):</b> <code>3.7 млн.</code>
<b>Тинькофф Банк:</b> <code>30 млн.</code>
<b>Банк Открытие:</b> <code>10 млн.</code>
<b>QIWI кошельки:</b> <code>22 млн.</code>
<b>ВкусВилл:</b> <code>2.5 млн.</code>
<b>Ашан (сотрудники):</b> <code>1.4 тыс.</code>
<b>Wildberries (фулл):</b> <code>50 млн.</code>
<b>Евросеть:</b> <code>20 млн.</code>
<b>Ситилинк:</b> <code>2.8 млн.</code>
<b>Гемотест (лаборатория):</b> <code>400 тыс.</code>
<b>Столото (лотореи):</b> <code>3 млн.</code>
<b>ВКонтакте (устаревшие базы):</b> <code>100 млн+.</code>
<b>Яндекс (устаревшие хэши):</b> <code>50 млн.</code>
<b>Дром (Drom.ru):</b> <code>12.5 млн.</code>
<b>Билеты.ру (концерты):</b> <code>7 млн.</code>
<b>Спортмастер:</b> <code>2.3 млн.</code>
<b>М.Видео (сотрудники):</b> <code>1.3 тыс.</code>
<b>Национальная Медиа Группа:</b> <code>1.1 тыс.</code>
<b>Совкомбанк:</b> <code>5.7 млн.</code>
<b>ТКС (Tinkoff Black):</b> <code>30 млн.</code>
<b>IVI (ivi.ru):</b> <code>5.5 млн.</code>
<b>Яндекс.Музыка:</b> <code>10 млн.</code>"""
            
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton("🛢All DataBase", url="https://xss-osint-database.onrender.com")
            btn2 = types.InlineKeyboardButton("🔙Back", callback_data='back_to_main')
            markup.add(btn1, btn2)
            
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption=database_text,
                parse_mode='HTML',
                reply_markup=markup
            )
            logger.info(f"User {call.from_user.id} clicked Database")
        elif call.data == "webchat":
            bot.answer_callback_query(call.id, "Web-Chat")
            logger.info(f"User {call.from_user.id} clicked Web-Chat")
        elif call.data == "profile":
            bot.answer_callback_query(call.id, "Profile")
            logger.info(f"User {call.from_user.id} clicked Profile")
        elif call.data == "buysub":
            bot.answer_callback_query(call.id, "Buy sub")
            logger.info(f"User {call.from_user.id} clicked Buy sub")
        elif call.data == "owner":
            bot.answer_callback_query(call.id, "Owner")
            logger.info(f"User {call.from_user.id} clicked Owner")
        elif call.data == "admin":
            bot.answer_callback_query(call.id, "Admin - Panel")
            logger.info(f"User {call.from_user.id} clicked Admin Panel")
        elif call.data == "back_to_main":
            markup = types.InlineKeyboardMarkup(row_width=3)
            btn1 = types.InlineKeyboardButton("🔍OSINT", callback_data='osint')
            btn2 = types.InlineKeyboardButton("🛢DataBase", callback_data='database')
            btn3 = types.InlineKeyboardButton("🌐Web-Chat", callback_data='webchat')
            btn4 = types.InlineKeyboardButton("🧧Profile", callback_data='profile')
            btn5 = types.InlineKeyboardButton("💳Buy sub", callback_data='buysub')
            btn6 = types.InlineKeyboardButton("🎫Owner", callback_data='owner')
            markup.add(btn1, btn2, btn3)
            markup.add(btn4, btn5, btn6)
            if call.from_user.id == OWNER_ID:
                btn7 = types.InlineKeyboardButton("💻Admin - Panel", callback_data='admin')
                markup.add(btn7)
            caption = "<b>xss - osint: информационный агрегатор. Базы: 10 ТБ (публичные данные) + 17 ТБ (закрытые источники), Google dorking.\nИспользование - исключительно в исследовательских целях. Ответственность лежит на пользователе.</b>"
            
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption=caption,
                parse_mode='HTML',
                reply_markup=markup
            )
            logger.info(f"User {call.from_user.id} clicked Back to main")
            
    except Exception as e:
        logger.error(f"Error in callback_query for user {call.from_user.id}, data {call.data}: {str(e)}", exc_info=True)
        try:
            bot.answer_callback_query(call.id, f"Error: {str(e)[:50]}")
        except:
            pass

if __name__ == '__main__':
    logger.info("Bot started polling...")
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        logger.error(f"Polling error: {str(e)}", exc_info=True)
