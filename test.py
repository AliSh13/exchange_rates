import unittest
from ruble import cur_all, get_html, get_rate, send_message

class TestRuble(unittest.TestCase):
    """Проверяет работу скрипта"""
    def test_output_all_currencies(self):
        all_currencies = cur_all()
        self.assertIsNotNone(all_currencies)

unittest.main()
