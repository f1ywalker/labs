def z1():
    password = input("Введите пароль: ")
    confirm = input("Подтвердите пароль: ")
    if password == confirm:
        print("Пароль принят")
    else:
        print("Пароль не принят")



def z2():
    seat = int(input("Введите номер места: "))

    if seat % 2 == 0:
        if seat <= 36:
            print("Нижнее место в купе")
        else:
            print("Нижнее место в боковом отсеке")
    else:
        if seat <= 35:
            print("Верхнее место в купе")
        else:
            print("Верхнее место в боковом отсеке")



def z3():
    year = int(input("Введите год: "))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"Год {year} - високосный")
    else:
        print("Это год не високосный")


def z4():
    color1 = input("Введите первый основной цвет для смешивания: ")
    color2 = input("Введите второй основной цвет для смешивания: ")

    if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
        print("Фиолетовый")
    elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
        print("Оранжевый")
    elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
        print("Зеленый")
    else:
        print("Ошибка: введите названия цветов красный, синий или желтый")

z1(), z2(), z3(), z4()
