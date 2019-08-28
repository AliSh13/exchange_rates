#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import re
import os
import sys

class GetRates():
    def __init__(self, currency='USD'):
        self.currency = currency

    def get_html(self):
        url = 'https://www.cbr.ru/currency_base/daily/'
        r = requests.get(url)
        return r.text

    def get_rate(self, currency):
        """Находит курс выбранной валюты. По умолчанию - USD"""
        currency = currency.upper()
        soup = BeautifulSoup(self.get_html(), 'lxml')
        result = soup.find('td', text=currency).find_parent().find_all('td')[-1].text
        return result

    def cur_all(self):
        'Выводит список всех возможных валют'
        soup = BeautifulSoup(self.get_html(), 'lxml')
        abbreviation = soup.find_all('td', text=re.compile('[A-Z]'))
        currencies = soup.find_all('td', text=re.compile('[А-я]'))
        n = 0
        for abr in abbreviation:
            print(abr.text + '-' + currencies[n].text)
            n += 1

    def send_message(self, message):
        """Выводит сообщение в терминал"""
        os.system('echo "{}"'.format(message))

    def run(self):
        """ Запускает скрипт, предварительно проверив наличие аргументов"""
        if len(sys.argv) > 1:
            if sys.argv[1].upper() == 'ALL':
                return self.cur_all()
            self.currency = sys.argv[1]

        """if self.currency.upper() == 'ALL':
            return self.cur_all()"""

        try:
            rate = self.get_rate(self.currency)
            self.send_message(rate)
        except AttributeError:
            #перехватывает исключение не корректного атрибута.
            messge = ('Не корректная абривеатура валюты. Для вывода всех возможных воспользуйтесь "all" ')
            self.send_message(messge)



if __name__ == '__main__':
    main = GetRates()
    main.run()
