import os
import random
import threading
import time
import warnings
import logging
from urllib3.exceptions import InsecureRequestWarning

import requests

import telebot
from telebot import types

from dotenv import load_dotenv

from api import send_request_to_hsc

from db import APIsettings, create_database_table_if_not_exists, set_last_settings


load_dotenv()
dates = ['2023-11-11', '2023-11-12', '2023-11-13', '2023-11-14', '2023-11-15', '2023-11-16', '2023-11-17', '2023-11-18']
buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
buttons.add(
    types.KeyboardButton(text='/logging'),
)


def send_request():
    conn = create_database_table_if_not_exists()
    cur = conn.cursor()

    for date in dates:

        response = send_request_to_hsc(date)
        if len(response['rows']) != 0:
            participants = cur.execute('SELECT user_id FROM participants').fetchall()
            for participant in participants:
                for a_time in response['rows']:
                    bot.send_message(participant[0],
                                     f'<b>Available as of {date} on time: {a_time["chtime"]}</b>\nhttps://eq.hsc.gov.ua/site/step')
        else:
            logging.warning(f'Date {date} is empty!')
        time.sleep((random.randint(2, 4) + random.random()) * 60)
    conn.close()


def register_participant(update):
    conn = create_database_table_if_not_exists()
    cur = conn.cursor()
    user_id = update.from_user.id
    
    cur.execute('SELECT user_id FROM participants WHERE user_id = ?', (user_id,))
    existing_user = cur.fetchone()
    if existing_user:
        return
    else:
        cur.execute('INSERT INTO participants (user_id) VALUES (?)', (user_id,))
        logging.info(f'User register: {update.from_user.username}')
    conn.commit()


def send_message(user_id, message):
    bot.send_message(user_id, message, reply_markup=buttons)


bot = telebot.TeleBot(os.getenv('TOKEN'), parse_mode='html')


@bot.message_handler(commands=['start'])
def start(update):
    register_participant(update)
    send_message(update.from_user.id, 'The bot has been started!')


@bot.message_handler(commands=['logging'])
def log(update):
    log_file = open('logging.log', 'rb')
    bot.send_document(update.from_user.id, log_file, reply_markup=buttons)


@bot.message_handler(commands=['apisettings'])
def change_settings(update):
    
    def split_value(text: str, spliting_from: str) -> str:
        return text.split(spliting_from)[1].split(';')[0]
    
    text = update.text
    cookies = text.split('Cookie: ')[1].split(" \\")[0]
    x_csrf_token = text.split('X-CSRF-Token: ')[1].split("' \\")[0]
    
    _gid = split_value(cookies, '_gid=')
    _gat = split_value(cookies, '_gat=')
    _ga_3GVV2WPF7F = split_value(cookies, '_ga_3GVV2WPF7F=')
    WEBCHSID2 = split_value(cookies, 'WEBCHSID2=')
    _csrf = split_value(cookies, '_csrf=')
    
    set_last_settings(APIsettings(_gid, _gat, _ga_3GVV2WPF7F, WEBCHSID2, _csrf, x_csrf_token))


def send_request_thread():
    while True:
        try:
            send_request()
        except requests.exceptions.JSONDecodeError:
            logging.critical('CHANGE TOKEN!')
            send_message(331253781, 'CHANGE TOKEN! <b>ERROR</b>')
            time.sleep(60 * 60 * 2)
        except Exception as error:
            logging.error(error)
            time.sleep(20 * 60)
        else:
            time.sleep((4 + random.random()) * 60)


if __name__ == "__main__":
    logging.basicConfig(filename='logging.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    warnings.filterwarnings("ignore", category=InsecureRequestWarning)
    
    request_thread = threading.Thread(target=send_request_thread)
    request_thread.daemon = True
    request_thread.start()

    bot.polling()
    warnings.resetwarnings()
