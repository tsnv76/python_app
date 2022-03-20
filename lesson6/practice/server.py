"""
Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> - TCP-порт для работы (по умолчанию использует порт 7777);
-a <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""
import argparse
import json
import logging
import log.config_server_log
import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from decors import log
from sys import argv

from common.utils import get_message, send_message
from common.variables import PRESENCE, ACTION,  TIME, USER, ACCOUNT_NAME, \
    MAX_CONNECTIONS, RESPONSE,  RESPONDEFAULT_IP_ADDRESS, ERROR, DEFAULT_PORT
from errors import IncorrectDataRecivedError

SERVER_LOGGER = logging.getLogger('server')


@log
def process_client_message(msg):
    """
    Прверяет корректность словаря от клиента
    :param msg:
    :return:
    """
    if ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg and USER in msg \
            and msg[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONDEFAULT_IP_ADDRESS: 400,
        ERROR: 'Bad request'
    }


@log
def create_arg_parser():
    """
        Парсер аргументов командной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser


def main():
    """
    Функция работы программы через командную строку.
    Использование:
    server.py -p < номер порта в диапазоне [1024-65535} > -a < IP адрес, который слушает сервер >
    Если нет параметров - используются параметры, заданные по-умолчанию
    :return:
    """
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    if not 1023 < listen_port < 65636:
        SERVER_LOGGER.critical(f' Попытка запуска сервера с указанием неподходящего порта '
                               f'{listen_port}. Допустимы значения с 1024 до 65535')
        sys.exit()
    SERVER_LOGGER.info(f'Запущен сервер. Порт для подключений клиентов: {listen_port}. '
                       f'Подключения принимаются на адрес: {listen_address} ('
                       f'Если адрес не указан - принимаются соедитнения с любых адресов!)')

    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((listen_address, listen_port))
    s.listen(MAX_CONNECTIONS)

    while True:
        client, client_addr = s.accept()  # Принять запрос на соединение
        SERVER_LOGGER.info(f'Установлено соединение с клиентом {client_addr}.')
        try:
            print(f'Получен запрос на соединение от {client_addr} ')
            mess_from_client = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение {mess_from_client}')
            print(mess_from_client)
            response = process_client_message(mess_from_client)
            SERVER_LOGGER.info(f'Сформирован ответ клиенту {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_addr} закрывается!')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать Json-строку, полученную от клиента {client_addr} '
                                f'Соединение закрывается')
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'От клиента {client_addr} приняты некорректные данные. '
                                f'Соединение закрывается')
        client.close()


if __name__ == '__main__':
    main()
