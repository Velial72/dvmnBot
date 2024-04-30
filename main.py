import logging

import requests
import urllib
from telegram.ext import Updater
from time import sleep

from logs import TelegramLogHandler
from environs import Env


def main():
    env = Env()
    env.read_env()
    bot = Updater(token=env.str('TG_TOKEN')).bot
    url = f"https://dvmn.org/api/long_polling/"
    headers = {
        'Authorization': f"Token {env('DVMN_TOKEN')}",
    }
    params = {
        'timestamp': None,
    }

    logging.basicConfig(
        handlers=[TelegramLogHandler(tg_bot=bot, chat_id=env('CHAT_ID'))]
    )

    logging.warning("Бот запущен")
    
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            last_update = response.json()
            status = last_update['status']

            if status == 'found':
                acceptance = last_update['new_attempts'][0]['is_negative']
                lesson_title = last_update['new_attempts'][0]['lesson_title']
                lesson_url = last_update['new_attempts'][0]['lesson_url']
                if acceptance:
                    bot.send_message(
                        text=f'У вас проверили работу {lesson_title}\n{lesson_url}\nК сожалению, в работе нашлись ошибки.',
                        chat_id=env('CHAT_ID')
                    )

                else:
                    bot.send_message(
                        text=f'У вас проверили работу {lesson_title}\n{lesson_url}\nПреподователю все понравилось, можно приступать к следующему уроку!',
                        chat_id=env('CHAT_ID')
                    )

                timestamp = last_update['last_attempt_timestamp']
                params['timestamp'] = timestamp

            else:
                timestamp = last_update['timestamp_to_request']
                params['timestamp'] = timestamp

        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            logging.exception("Бот упал с ошибкой")
            sleep(120)


if __name__ == '__main__':
    main()
