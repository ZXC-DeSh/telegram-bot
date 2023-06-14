from pprint import pprint

goods = [
    {
    'name': 'Iphone 14',
    'brand': 'Apple',
    'price': 1200
    },
    {
    'name': 'Samsung Galaxy A53',
    'brand': 'Samsung',
    'price': 600
    },
    {
    'name': 'Xiaomi Mi 10T',
    'brand': 'Xiaomi',
    'price': 400
    }
    ]

if __name__ == '__main__':
    goods = [
        {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200
        },
        {
        'name': 'Samsung Galaxy A53',
        'brand': 'Samsung',
        'price': 600
        },
        {
        'name': 'Xiaomi Mi 10T',
        'brand': 'Xiaomi',
        'price': 400
        }
        ]


    # def item_price(item):
    # return item['price']


    print(sorted(goods, key=lambda item: item['price']))

    # все товары бренда Apple
    apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
    print(apple_list)

    # функцию map
    numbers = ['1', '2', '3', '4', '5']
    numbers = list(map(int, numbers))
    print(numbers)




    names = ['даниил', "Никита","Настя"]
    surnames = ["Петров","Иванов","Смирнова"]

    full_names = list(map(lambda name, surname: f'{name} {surname}', names, surnames))
    print(full_names)



    indexed_goods = []
    for index, item in enumerate(goods):
        indexed_goods.append({index : item})
    print(indexed_goods)

    patronymics = ['Mixail', 'Vitalievich', 'Ivanovich']
    for name, surname, patronymic in zip(names, surnames, patronymics):
        print(surname, name, patronymic)