def z1():
    import random
    spisok = []
    for i in range(5):
        spisok.append(random.randrange(1,20))
    n = int(input("Введите число: "))
    if n in spisok:
        print(spisok, n, "\nПоздавляю, вы угадали!")
    else:
        print(spisok,n, "\nТакого числа нет в списке")


def z2():
    import random
    spisok = []
    duplicates = []
    for i in range(10):
        spisok.append(random.randrange(1,20))
    for element in spisok:
        if spisok.count(element) > 1:
            if element not in duplicates:
                duplicates.append(element)
    if duplicates:
        print("Список:", spisok, "\nПовторяющиеся элементы в списке:", duplicates)
    else:
        print("Повторяющихся элементов в списке нет")


def z3():
    days = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
    weekends = int(input("Сколько выходных дней вы хотите?"))
    end = days[-weekends:]
    day = days[:len(days) - weekends]
    print("Ваши выходные дни: ", *end, "\nВаши рабочие дни: ", *day)

def z4():
    import random
    g1 = ["Иванов", "Петров", "Смирнов", "Кузнецов", "Попов"]
    g2 = ["Соколов", "Васильев", "Иванов", "Козлов", "Зайцев"]
    t1 = random.sample(g1, 2)
    t2 = random.sample(g2, 2)
    team = tuple(sorted(t1 + t2))
    length = len(team)
    count = team.count("Иванов")
    if count == 0:
        print(g1, "\n", g2, "\n", team, "\n", length, "\n", "Студент Иванов не в команду не входит")
    else:
        print(g1, "\n", g2, "\n", team, "\n", length, "\n", "Студент Иванов состоит в команде", count, "раз(а)")

z1(), z2(), z3(), z4()