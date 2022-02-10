"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о
заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее
значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    """
        Функция записывает данные в виде словаря в  JSON-файл;
        - item, quantity, price, buyer, date: передаваемые данные

    """

    with open('orders.json', encoding='utf-8') as f_n:
        dict_to_json = json.load(f_n)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
        print(dict_to_json)
    with open('orders.json', 'w', encoding='utf-8') as f_w:
        json.dump(dict_to_json, f_w, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    write_order_to_json('Материнская плата', 10, 6000, 'Иванов', '01.02.2022')
    write_order_to_json('Процессор', 20, 7000, 'Петров', '22.01.2022')
    write_order_to_json('Оперативная память', 15, 2500, 'Сидоров', '11.02.2022')
    write_order_to_json('Жесткий диск', 100, 1500, 'Васечкин', '20.01.2022')

