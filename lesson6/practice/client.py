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
import argparse
import json
import logging
import sys

import log.config_client_log
from json import JSONDecodeError
from socket import socket, AF_INET, SOCK_STREAM
import time
from decors import log


from common.utils import send_message, get_message
from common.variables import PRESENCE, ACTION, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR, DEFAULT_PORT, DEFAULT_IP_ADDRESS, ENCODING
from errors import ReqFieldMissingError

CLIENT_LOGGER = logging.getLogger('client')


@log
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
    CLIENT_LOGGER.debug(f'Формируем {PRESENCE} сообщение для пользователя {account_name}')
    return message


@log
def server_ans(alert):
    """
    Функция проверяет ответ от сервера
    :param alert:
    :return:
    """
    CLIENT_LOGGER.debug(f'Разбираем сообщение от сервера {alert}')
    if RESPONSE in alert:
        if alert[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {alert[ERROR]}'
    raise ReqFieldMissingError(RESPONSE)


@log
def create_arg_parser():
    """
        Парсер аргументов командной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser



def main():
    """
    Функция работы программы через командную строку.
    Использование:
    client.py -p < номер порта в диапазоне [1024-65535} > -a < IP адрес клиента >
    Если нет параметров - используются параметры, заданные по-умолчанию
    :return:
    """
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port

    if not 1023 < server_port < 65636:
        CLIENT_LOGGER.critical(f' Попытка запуска клиента с указанием неподходящего порта. '
                               f'{server_port}. Допустимы значения с 1024 до 65535. Клиент завершается')
        sys.exit()
    CLIENT_LOGGER.info(f'Запущен клиент с параметрами: '
                       f'Адрес сервера: {server_address} , порт: {server_port}')
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((server_address, server_port))
        msg_to_server = create_presence()
        send_message(client, msg_to_server)
        answer = server_ans(get_message(client))
        CLIENT_LOGGER.info(f'Принят ответ от сервера {answer}.')
        print(answer)
    except json.JSONDecodeError:
        CLIENT_LOGGER.error(f'Ошибка декодирования сообщения от сервера.')
    except ConnectionRefusedError:
        CLIENT_LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port}.')
    except ReqFieldMissingError as missing_error:
        CLIENT_LOGGER.error(f'В ответе сервера отсутствует необходимое поле '
                            f'{missing_error.missing_field}.')


if __name__ == '__main__':
    main()
