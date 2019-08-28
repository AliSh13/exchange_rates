import unittest
import os
import sys
from ruble import GetRates



class TestRuble(unittest.TestCase):
    """Проверяет работу скрипта"""
    """def setUp(self):
        self.ruble = GetRate()"""

    def test_default_arg(self):
        "Проверяет, что по умолчанию выводится курс USD"
        usd = GetRates()
        self.assertEqual(usd.run(), GetRates('USD').run())

    def test_of_invalid_arg(self):
        "Проверяет правильность вывода при некорректном аргументе"
        invalid_arg = GetRates('any arg')
        messge = 'Не корректная абривеатура валюты. Для вывода всех возможных воспользуйтесь all'
        self.assertEqual(invalid_arg.run(), GetRates().send_message(messge))

        


unittest.main()
