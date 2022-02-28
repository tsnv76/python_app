def words_encoding(word):
    try:
        result1 = bytes(word, 'ascii')
        print(f'Содержимое -> "{result1}"')
        return result1
    except Exception as e:
        print(f'ОШИБКА! Слово "{word}" невозможно записать в байтовом типе: {e}')


words = ['attribute', 'класс', 'функция', 'type']

for item in words:
    words_encoding(item)

