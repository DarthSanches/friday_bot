import telebot
import time

# our friday bot
FRIDAY_BOT_TOKEN = "1311122903:AAGtOdh2YltJ_nl1dedCFRt2VWTfai53ZpE"

# our chat
CHELNY_CHAT_ID = 1001596779053

#friday_bot
fb = telebot.TeleBot(FRIDAY_BOT_TOKEN)

fb.sendMessage(CHELNY_CHAT_ID, "Приветствую, свидетели! Я бот пятницы и Юсуп мой прораб!")

def listener(messages):
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            fb.send_message(chatid, text)

fb.set_update_listener(listener)
fb.polling()

fb.polling(none_stop=True)

fb.polling(interval=3)

while True:
    pass
