def word_encoding_decoding(word):
    return f'Слово => {word}\n В байтовом виде => {word.encode("utf8")}\n ' \
           f'Раскодированная обратно в строку  => {word.encode("utf8").decode()}\n'


words = ['разработка', 'администрирование', 'protocol', 'standard']

for item in words:
    print(word_encoding_decoding(item))

