from chardet import detect

strings = ['сетевое программирование',
          'сокет',
          'декоратор']

file_name = 'test_file.txt'
f = open(file_name, 'w', encoding='utf-8')
for item in strings:
    f.write(item + '\n')
    print(f'Записываем в файл {file_name} строку "{item}"')
f.close()
print('______________________________')
print(f'Содержимое файла {file_name}')
with open(file_name, 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('Кодировка: ', encoding)

with open(file_name, encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')

