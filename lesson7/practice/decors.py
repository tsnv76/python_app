"""
    Декораторы
"""
import logging
import sys
import traceback

if sys.argv[0].find('client.py') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func_log):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        ret = func_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_log.__name__} с параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_log.__module__}. '
                     f'Вызов из функции {traceback.format_stack()[0].strip().split()[-1]} ')
        return ret
    return log_saver
