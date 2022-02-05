# def word_encoding()

words = ['class', 'function', 'method', 'еее']
# print(eval("'b' + '\'' + words[1]"))
for item in words:
    try:
        word = 'b' + "'" + item
        print(word, type(word))
    except Exception as e:
        print(f'ОШИБКА! Слово "{item}" невозможно записать в байтовом типе: {e}')
    # print(f'Содержимое -> {'item}, lлина строки = {len(item)},  тип данных -> {type(item)}\n')

