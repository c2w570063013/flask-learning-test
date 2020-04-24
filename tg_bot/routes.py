from flask import Blueprint
# import telegram
# import json
# import re
import requests
from flask import request
from flask import Response

tg = Blueprint('tg', __name__, url_prefix='/tg')

bot_key = '1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk'
top_10btc_api = 'https://nomics.com/data/currencies/ticker?include-transparency=false&interval=1d,30d&labels=0&limit=10&quote-currency=USD&start=0'
cryptoprice = '/cryptoprice'
cPrice_notice_higher_than = '/cPrice_notice_higher_than'
cPrice_notice_lower_than = '/cPrice_notice_lower_than'
valid_commands = [
    '/cryptoprice',
    '/cPrice_notice_higher_than',
    '/cPrice_notice_lower_than'
]


# test
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/sendMessage?chat_id=324171792&text=how%20are%20you
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/getUpdates
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/getMe
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/getWebhookInfo
# https://api.telegram.org/bot1051400474:AAEkNqkdvOem7_mLJwpnjSHEcrsYSbuE8Fk/setWebhook?url=https://crosseverycorner.xyz/tg/web_hook
@tg.route('/setup')
def setup():
    return 'hello'


def parse_msg(msg):
    chat_id = msg['message']['chat']['id']
    tex = msg['message']['text']
    command = tex
    param = ''
    space_p = tex.find(' ')
    if space_p > 0:
        command = tex[:space_p]
        param = tex[tex.rfind(' ') + 1:]
    return chat_id, tex, command, param


def send_msg(chat_id, text='bla-bla-bal--'):
    url = f'https://api.telegram.org/bot{bot_key}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'markdown'}
    r = requests.post(url, json=payload)
    return r


def get_top10_crypto():
    res = requests.get(top_10btc_api).json()
    final_list = []
    price_date = res['items'][0]['price_date']
    for i in res['items']:
        final_list.append({
            'name': i['symbol'],
            'price': i['price'],
            '1d_price_change_pct': i['1d']['price_change_pct'],
            '30d_price_change_pct': i['30d']['price_change_pct']
        })
    return price_date, final_list


def crypto_currency_price(chat_id):
    price_date, final_list = get_top10_crypto()
    text = '*' + price_date + '*' + "\n" + '*crypto   price   1day_change_pct   30d_change_pct*' + "\n"
    for i in final_list:
        price = str(round(float(i['price']), 4))
        d_change_pct = str(round(float(i['1d_price_change_pct']) * 100, 1)) + '%'
        d30_change_pct = str(round(float(i['30d_price_change_pct']) * 100, 1)) + '%'
        text += i['name'] + '   *' + price + '*   ' + d_change_pct + '   ' + d30_change_pct + "\n"
    send_msg(chat_id, text)


@tg.route('/web_hook', methods=['POST', 'GET'])
def web_hook():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, tex, command, param = parse_msg(msg)
        if command not in valid_commands:
            send_msg(chat_id, 'command doesn\'t exist')
            return Response('ok', status=200)
        if command == cryptoprice:
            crypto_currency_price(chat_id)

        return Response('ok', status=200)
    else:
        return 'hello world'
