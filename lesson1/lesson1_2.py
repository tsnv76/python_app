def words_encoding(word):
    st = "'" + word + "'"
    try:
        result1 = eval('b' + st)
        print(f'Содержимое -> "{result1}", длина строки = {len(result1)},  тип данных -> {type(result1)}\n')
        return result1
    except Exception as e:
        print(f'ОШИБКА! Слово "{word}" невозможно записать в байтовом типе: {e}')
    


words = ['омлром', 'class', 'function', 'method', 'олывсрфывос']
for item in words:
    words_encoding(item)



