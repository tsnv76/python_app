import json
import sys

from errors import IncorrectDataRecivedError
from .variables import MAX_PACKAGE_LENGTH, ENCODING

sys.path.append('../')
from decors import log


@log
def get_message(client):
    """
    Прием и декодирование сообщения
    Принимает байты - выдает словарь
    Если принято что-то другое - выдает ошибку
    :param client: сообщение
    :return: response
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise IncorrectDataRecivedError
    raise IncorrectDataRecivedError


def send_message(sock, message):
    """
    Отправление сообщения
    Принимает словарь и отправляет
    :param sock:
    :param message:
    :return:
    """
    if isinstance(message, dict):
        jmsg = json.dumps(message)
        sock.send(jmsg.encode(ENCODING))
    else:
        raise TypeError
