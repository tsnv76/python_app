def type_str(word):
    return f'Слово "{word}" -> Типа {type(word)}'


words = ['разработка', 'сокет', 'декоратор']

for item in words:
    print(type_str(item))

words_utf8 = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
              '\u0441\u043e\u043a\u0435\u0442',
              '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

print('---------- Преобразованные в формат Unicode -----------')
for item in words_utf8:
    print(type_str(item))

