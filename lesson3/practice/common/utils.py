import json
from .variables import MAX_PACKAGE_LENGTH, ENCODING


def convert_dict_to_bytes(msg):
    if isinstance(msg, dict):
        jmsg = json.dumps(msg)
        bmsg = jmsg.encode(ENCODING)
        return bmsg
    else:
        raise TypeError


def convert_bytes_to_dict(msg):
    if isinstance(msg, bytes):
        jmsg = msg.decode(ENCODING)
        dict_msg = json.loads(jmsg)
        if isinstance(dict_msg, dict):
            return dict_msg
        raise ValueError
    raise ValueError


def get_message(client):
    """
    Прием и декодирование сообщения
    Принимает байты - выдает словарь
    Если принято что-то другое - выдает ошибку
    :param client: сообщение
    :return: response
    """
    encoding_response = client.recv(MAX_PACKAGE_LENGTH)
    # байты переводим в словарь
    response = convert_bytes_to_dict(encoding_response)
    return response


def send_message(sock, message):
    """
    Отправление сообщения
    Принимает словарь и отправляет
    :param sock:
    :param message:
    :return:
    """

    # переводим словарь в байты и отправляем сообщение
    sock.send(convert_dict_to_bytes(message))
