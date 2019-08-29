import unittest
import os
import sys
import requests
from ruble import GetRates



class TestRuble(unittest.TestCase):
    """Проверяет работу скрипта"""
    def setUp(self):
        self.ruble = GetRates()

    def test_default_arg(self):
        "Проверяет, что по умолчанию выводится курс USD"
        self.assertEqual(self.ruble.run(), GetRates('USD').run())

    def test_of_invalid_arg(self):
        "Проверяет правильность вывода при некорректном аргументе"
        invalid_arg = GetRates('any arg')
        messge = 'Не корректная абривеатура валюты. Для вывода всех возможных воспользуйтесь all'
        self.assertEqual(invalid_arg.run(), self.ruble.send_message(messge))

    def test_register(self):
        "Проверяет что бы любой регистр аргумента работал нормально"
        all = GetRates('all')
        for arg in ['All', 'all', 'ALL', 'alL', 'aLL']:
            self.assertEqual(GetRates(arg).run(), all.run())



url = 'https://www.cbr.ru/currency_base/daily/'
r = requests.get(url)
if r.status_code == 200:
    '''Перед проверкой обеждаемся что есть подключение'''
    unittest.main()
