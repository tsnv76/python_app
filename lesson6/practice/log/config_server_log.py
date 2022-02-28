"""Кофнфигурация серверного логгера"""

import sys
import os
import logging
import logging.handlers
from common.variables import LOGGING_LEVEL
sys.path.append('../')

# создаём формировщик логов (formatter):
SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
"""
    TimedRotatingFileHandler(filename, when='h', interval=1, 
                         backupCount=0, encoding=None, 
                         delay=False, utc=False, atTime=None)
    Параметры:
        filename - имя файла лога,
        when='D' - тип интервала, означает день 
        interval=1 - интервал времени,
        backupCount=0 - количество хранимых логов,
        encoding=None - кодировка файла
        delay=False - задержка открытия файла,
        utc=False - использовать время UTC,
        atTime=None -
                                 
"""
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)

# создаём регистратор и настраиваем его
LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
