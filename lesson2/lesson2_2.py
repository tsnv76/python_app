import json


def write_order_to_json(item, quantity, price, buyer, date):
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
    with open('orders1.json', 'w', encoding='utf-8') as f_w:
        json.dump(dict_to_json, f_w, indent=4)


if __name__ == "__main__":
    write_order_to_json('Материнская плата', 10, 6000, 'Smith', '01.02.2022')
    write_order_to_json('Процессор', 20, 7000, 'Bern', '22.01.2022')
    write_order_to_json('Оперативная память', 15, 2500, 'Ostin', '11.02.2022')
    write_order_to_json('Жесткий диск', 100, 1500, 'Garry', '20.01.2022')
