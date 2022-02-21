"""
    Unit-тесты клиента
"""

import unittest
import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))

from client import create_presence
from common.variables import TIME, ACTION, PRESENCE, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, ENCODING
from client import server_ans


class TestClass(unittest.TestCase):
    """
        Класс с тестами
    """
    def test_def_create_presense(self):
        """"
            Тест корректного запроса
        """
        test = create_presence()
        test[TIME] = 2
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 2, USER: {ACCOUNT_NAME: 'Guest'}, 'encoding': ENCODING})

    def test_200_answer(self):
        """
            Тест ответа 200
        """
        self.assertEqual(server_ans({RESPONSE: 200}), '200 : OK')

    def test_400_answer(self):
        """
            Тест ответа 400
        """
        self.assertEqual(server_ans({RESPONSE: 400, ERROR: 'Bad Request'}), f'400 : {ERROR}')

    def test_no_response(self):
        """
             Тест выпадение исключения без поля RESPONSE
        """
        self.assertRaises(ValueError, server_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
