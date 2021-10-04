import telebot
import time

#friday_bot token
fb = telebot.TeleBot("1311122903:AAGtOdh2YltJ_nl1dedCFRt2VWTfai53ZpE")

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