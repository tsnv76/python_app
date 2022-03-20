"""
Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> - TCP-порт для работы (по умолчанию использует порт 7777);
-a <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from json import JSONDecodeError
from sys import argv

from common.utils import get_message, send_message
from common.variables import PRESENCE, ACTION,  TIME, USER, ACCOUNT_NAME, \
    MAX_CONNECTIONS, RESPONSE,  RESPONDEFAULT_IP_ADDRESS, ERROR, DEFAULT_PORT


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


def main():
    """
    Функция работы программы через командную строку.
    Использование:
    server.py -p < номер порта в диапазоне [1024-65535} > -a < IP адрес, который слушает сервер >
    Если нет параметров - используются параметры, заданные по-умолчанию
    :return:
    """

    try:
        if '-p' in argv:
            listen_port = int(argv[argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' нужно указать номер порта.')
        exit(1)
    except ValueError:
        print('Значение порта - число в диапазоне от 1024 до 65535.')
        exit(1)

    try:
        if '-a' in argv:
            listen_address = argv[argv.index('-a') + 1]
        else:
            listen_address = '0.0.0.0'
    except IndexError:
        print('После параметра -\'a\' нужно указать IP адрес, который будет слушать сервер ')
        exit(1)

    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((listen_address, listen_port))
    s.listen(MAX_CONNECTIONS)

    while True:
        client, client_addr = s.accept()  # Принять запрос на соединение
        try:
            print("Получен запрос на соединение от %s" % str(client_addr))
            mess_from_client = get_message(client)
            print(mess_from_client)
            response = process_client_message(mess_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, JSONDecodeError):
            print('Сообщение не корректное')
            client.close()


if __name__ == '__main__':
    main()
