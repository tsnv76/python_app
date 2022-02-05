def words_encoding(word):
    try:
        result1 = bytes(word, 'ascii')
        print(f'Содержимое -> "{result1}", длина строки = {len(result1)},  тип данных -> {type(result1)}\n')
    except Exception as e:
        print(f'ОШИБКА! Слово "{word}" невозможно записать в байтовом типе: {e}')


words = ['омлром', 'class', 'function', 'method', 'олывсрфывос']
for item in words:
    words_encoding(item)


