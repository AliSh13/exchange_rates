#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import re
import os
import sys

class GetRates():
    def __init__(self, currency='USD', units='1'):
        self.currency = currency
        self.units = units

    def get_html(self):
        url = 'https://www.cbr.ru/currency_base/daily/'
        r = requests.get(url)
        return r.text

    def get_rate(self, currency, units):
        """Находит курс выбранной валюты(по умолчанию - USD) и приводит к читаемому виду. """
        currency = currency.upper()
        soup = BeautifulSoup(self.get_html(), 'lxml')
        result = soup.find('td', text=currency).find_parent().find_all('td')[-1].text
        result = float(result.replace(',','.')) * float(units)
        return "{0:3.2f} руб.".format(result)

    def cur_all(self):
        'Выводит список всех возможных валют'
        soup = BeautifulSoup(self.get_html(), 'lxml')
        abbreviation = soup.find_all('td', text=re.compile('[A-Z]{3}'))
        currencies = soup.find_all('td', text=re.compile('[А-я]'))
        n = 0
        for abr in abbreviation:
            print(abr.text + '-' + currencies[n].text)
            n += 1

    def send_message(self, message):
        """Выводит сообщение в терминал"""
        os.system('echo "{}"'.format(message))

    def run(self):
        """ Запускает скрипт, предварительно проверив наличие аргументов и их допустимость"""
        try:
            arg = sys.argv
            if len(arg) == 2:
                self.currency = arg[1].upper()
            elif len(arg) == 3:
                self.currency = arg[1].upper()
                self.units = arg[2]


            if self.currency.upper() == 'ALL':
                return self.cur_all()
                """проверяем правильность аргументов"""
            if self.currency.isalpha() and self.units.isdigit():
                rate = self.get_rate(self.currency, self.units)
                self.send_message(rate)
            else:
                raise AttributeError

        except AttributeError:
            #перехватывает исключение не корректного атрибута.
            messge = ('Не корректная аббривеатура валюты. Для вывода всех возможных воспользуйтесь "all" ')
            self.send_message(messge)



if __name__ == '__main__':
    main = GetRates()
    main.run()
