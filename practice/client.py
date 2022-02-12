"""
Функционал.
Первая часть домашнего задания будет заключаться в реализации простого клиент-серверного взаимодействия по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
Функции клиента:
сформировать presence-сообщение;
отправить сообщение серверу;
получить ответ сервера;
разобрать сообщение сервера;
параметры командной строки скрипта client.py <addr> [<port>]:
addr - ip-адрес сервера;
port - tcp-порт на сервере, по умолчанию 7777.
"""
from json import JSONDecodeError
from socket import socket, AF_INET, SOCK_STREAM
import time
from sys import argv

from common.utils import get_message, send_message

from practice.common.variables import PRESENCE, ACTION, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR, DEFAULT_PORT, DEFAULT_IP_ADDRESS, ENCODING


def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос от клиента
    :param account_name:
    :return:
    """
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        },
        'encoding': ENCODING,
    }

    return message


def server_ans(alert):
    """
    Функция проверяет ответ от сервера
    :param alert:
    :return:
    """

    if RESPONSE in alert:
        if alert[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {alert[ERROR]}'
    raise ValueError


def main():
    """
    Функция работы программы через командную строку.
    Использование:
    client.py -p < номер порта в диапазоне [1024-65535} > -a < IP адрес клиента >
    Если нет параметров - используются параметры, заданные по-умолчанию
    :return:
    """
    try:
        server_address = argv[1]
        server_port = int(argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('Значение порта - число в диапазоне от 1024 до 65535.')
        exit(1)
    print(server_address, server_port)
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((server_address, server_port))
    msg_to_server = create_presence()
    send_message(client, msg_to_server)
    try:
        answer = server_ans(get_message(client))
        print(answer)
    except (ValueError, JSONDecodeError):
        print('Ошибка декодирования сообщения от сервера')


if __name__ == '__main__':
    main()
