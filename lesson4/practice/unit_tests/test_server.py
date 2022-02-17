"""
    Unit-тесты сервера
"""
import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import TIME, ACTION, PRESENCE, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, ENCODING, RESPONDEFAULT_IP_ADDRESS
from server import process_client_message


class TestServer(unittest.TestCase):
    """
        Тестируем функцию сервера
    """
    error_dict = {
        RESPONDEFAULT_IP_ADDRESS: 400,
        ERROR: 'Bad request'
    }
    correct_dict = {RESPONSE: 200}

    def test_chek_ok(self):
        """
            Проверяем запрос на корректность
        """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 2, USER: {ACCOUNT_NAME: 'Guest'}, 'encoding': ENCODING}),
            self.correct_dict,
        )

    def test_no_action(self):
        """
            Ошибка, если нет действия
        """
        self.assertEqual(process_client_message(
            {TIME: 2, USER: {ACCOUNT_NAME: 'Guest'}, 'encoding': ENCODING}),
            self.error_dict,
        )

    def test_wrong_action(self):
        """
            Ошибка, если неизвестное действия
        """
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: 2, USER: {ACCOUNT_NAME: 'Guest'}, 'encoding': ENCODING}),
            self.error_dict,
        )

    def test_no_time(self):
        """
            Ошибка, если нет штампа времени
        """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}, 'encoding': ENCODING}),
            self.error_dict,
        )

    def test_no_user(self):
        """
            Ошибка, если нет пользователя
        """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 2, 'encoding': ENCODING}),
            self.error_dict,
        )

    def test_unknown_user(self):
        """
            Ошибка, если пользователь не 'Guest'
        """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 2, USER: {ACCOUNT_NAME: 'Vasya Pupkin'}, 'encoding': ENCODING}),
            self.error_dict,
        )


if __name__ == '__main__':
    unittest.main()
