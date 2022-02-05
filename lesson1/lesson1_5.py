import platform
import subprocess
import chardet


def f_ping(item):
    result = subprocess.Popen(item, stdout=subprocess.PIPE)
    for line in result.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


param = '-n' if platform.system().lower() == 'windows' else '-c'
args = [['ping', param, '2', 'yandex.ru'],
        ['ping', param, '2', 'youtube.com']]
for item in args:
    print(f'Пингуем ресурс {item[3]}. Преобразовываем результаты из байтовового в строковый тип')
    f_ping(item)

