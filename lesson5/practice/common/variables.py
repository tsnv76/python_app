
"""
    Константы
"""

# Порт по-умолчанию для сетевого взаимодействия
import logging

DEFAULT_PORT = 7777

# IP адрес  по-умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'


# Максимальная очередь подключений
MAX_CONNECTIONS = 5

# Максимальная длина сообщения в байтах
MAX_PACKAGE_LENGTH = 1024

# Кодировка проекта
ENCODING = 'utf-8'

# Протокол JIM - основные ключи
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ALERT = 'alert'
ERROR = 'Bad Request'
RESPONDEFAULT_IP_ADDRESS = 'respondefault_ip_address'

# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG

