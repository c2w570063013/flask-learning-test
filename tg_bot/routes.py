from flask import Blueprint
# import telegram
# import json
# import re
import requests
from flask import request
from flask import Response

tg = Blueprint('tg', __name__, url_prefix='/tg')

bot_key = '1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk'


# test
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/sendMessage?chat_id=324171792&text=how%20are%20you
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/getUpdates
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/getMe
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/getWebhookInfo
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/setWebhook?url=https://crosseverycorner.xyz/tg/web_hook
@tg.route('/setup')
def setup():
    return 'hello world'


def parse_msg(msg):
    chat_id = msg['message']['chat']['id']
    tex = msg['message']['text']
    return chat_id, tex


def send_msg(chat_id, text='bla-bla-bal--'):
    url = f'https://api.telegram.org/bot{bot_key}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=payload)
    return r


@tg.route('/web_hook', methods=['POST', 'GET'])
def web_hook():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, tex = parse_msg(msg)
        send_msg(chat_id, 'test test test')

        return Response('ok', status=200)
    else:
        return 'hello world'
