def z1():
    n = int(input("Введите количество слов: "))
    result = ""
    for i in range(n):
        word = input("Введите слово: ")
        result += word + " "
    print("Результат:", result.strip())


def z2():
    result = ""
    while True:
        word = input("Введите слово или напишите 'stop', чтобы остановиться: ")
        if word == "stop":
            break
        result += word + " "
    print("Результат:", result.strip())


def z3():
    def get_word(word):
        return 'ф' in word.lower()
    while True:
        word = input("Введите слово или 'stop' для выхода: ")
        if word == 'stop':
            break
        if get_word(word):
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово…")

def z4():
    import random
    score = 0
    errors = 0
    while errors < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = input(f"{a} + {b} = ")

        if int(ans) == a + b:
            print("Правильно!")
            score += 1
        else:
            print("Ответ неверный")
            errors += 1

    print(f"Игра окончена. Правильных ответов: {score}")
z1(), z2(), z3(), z4()
