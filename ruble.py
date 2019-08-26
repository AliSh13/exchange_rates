#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import re
import os
import sys


def get_html():
    url = 'https://www.cbr.ru/currency_base/daily/'
    r = requests.get(url)
    return r.text

def get_rate(currency):
    """Находит курс выбранной валюты. По умолчанию - USD"""
    currency = currency.upper()
    soup = BeautifulSoup(get_html(), 'lxml')
    result = soup.find('td', text=currency).find_parent().find_all('td')[-1].text
    return result

def cur_all():
    'Выводит список всех возможных валют'
    soup = BeautifulSoup(get_html(), 'lxml')
    abbreviation = soup.find_all('td', text=re.compile('[A-Z]'))
    currencies = soup.find_all('td', text=re.compile('[А-я]'))
    n = 0
    for abr in abbreviation:
        print(abr.text + '-' + currencies[n].text)
        n += 1

def send_message(message):
    os.system('echo "{}"'.format(message))

def main(currency='USD'):
    if len(sys.argv) > 1:
        if sys.argv[1] == 'all':
            cur_all()
        currency = sys.argv[1]

    try:
        rate = get_rate(currency)
        send_message(rate)
    except AttributeError:
        rate = ('Не корректная абривеатура валюты. Для вывода всех возможных воспользуйтесь "all" ')
        send_message(rate)



if __name__ == '__main__':
    main()
