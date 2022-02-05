def words_encoding(word):
    try:
        print(f'Преобразованное слово: {word.encode(encoding="ascii")}')
        word.encode(encoding='ascii')

    except Exception as e:
        print(f'ОШИБКА! Слово "{word}" невозможно записать в байтовом типе: {e}')


words = ['attribute', 'класс', 'функция', 'type']

for item in words:
    words_encoding(item)
