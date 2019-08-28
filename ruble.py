#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import re
import os
import sys

class GetRate():
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

    def run(self, currency='USD'):
        """ Запускает скрипт, предварительно проверив наличие аргументов"""
        if len(sys.argv) > 1:
            if sys.argv[1] == 'all':
                return self.cur_all()
            currency = sys.argv[1]

        """if currency == 'all':
            self.cur_all()"""

        try:
            rate = self.get_rate(currency)
            self.send_message(rate)
        except AttributeError:
            #перехватывает исключение не корректного атрибута.
            rate = ('Не корректная абривеатура валюты. Для вывода всех возможных воспользуйтесь "all" ')
            self.send_message(rate)



if __name__ == '__main__':
    main = GetRate()
    main.run()
