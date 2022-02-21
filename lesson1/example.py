import locale
import platform
import subprocess

import chardet as chardet
from chardet import detect

print('1')

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
result = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in result.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

default_encoding = locale.getpreferredencoding()
print(default_encoding)

f = open('test.txt', 'w', encoding='utf-8')
f.write('тест тест тест')
f.close()

with open('test.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)

with open('test.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
print()
