def z1():
    import json
    with open('products.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
def z2():
    import json
    with open('products.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    name = input("Введите название нового продукта: ")
    price = float(input("Введите цену нового продукта: "))
    weight = float(input("Введите вес нового продукта: "))
    available = input("Есть ли продукт в наличии? (y/n): ")

    data['products'].append({
        'name': name,
        'price': price,
        'weight': weight,
        'available': available.lower() == 'y'
    })

    with open('products.json', 'w') as f:
        json.dump(data, f)

    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as f:
        ru_en_dict = {}
        for line in f:
            eng, rus = line.strip().split(' - ')
            rus_words = [w.strip() for w in rus.split(',')]
            for word in rus_words:
                if word in ru_en_dict:
                    ru_en_dict[word].append(eng)
                else:
                    ru_en_dict[word] = [eng]
    with open('ru-en.txt', 'w', encoding='utf-8') as f:
        for word in sorted(ru_en_dict.keys()):
            f.write(f"{word} – {', '.join(sorted(ru_en_dict[word]))}\n")
z1(), z2(), z3()