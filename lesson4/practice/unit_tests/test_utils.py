"""
    Unit-тесты утилит
"""
import json
import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import TIME, ACTION, PRESENCE, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, ENCODING
from common.utils import get_message, send_message


class TestSocket:
    """
        Тестовый класс для тестирования отправки и получения сообщений
    """
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoding_message = None
        self.received_message = None

    def send(self, message_to_send):
        """
            Тестовая функция отправки
        :param message_to_send: сообщение, отправляемое в socket
        :return:
        """
        json_test_message = json.dumps(self.test_dict)
        self.encoding_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, max_len):
        """
            Получаем данные из socket'а
        :param max_len:
        :return:
        """
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    """
        Тестируем основные функции
    """
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 2,
        USER: {
            ACCOUNT_NAME: 'test'
        },
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request',
    }

    def test_send_message_ok(self):
        """
             Тестируем функциюо корректной тправки
        :return:
        """
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoding_message, test_socket.received_message)

    def test_send_message_wrong(self):
        """
             Тестируем функцию отправки с ошибкой
        :return:
        """
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, "wring dictionary")

    def test_get_message_ok(self):
        """
            Тест функции корректного приема сообщения
        :return:
        """
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

    def test_get_message_wrong(self):
        """
            Тест функции не корректного приема сообщения
        :return:
        """
        test_sock_err = TestSocket(self.test_dict_recv_err)
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()
