word = input("Введите слово: ").lower()

with open('synonyms.txt', 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    found_word = False

    for line in lines:
        if word in line.lower():
            found_word = True
            print(line.strip())
            replace = input(f"Нравится синоним(ы): {line.strip().split(' - ')[1]}? (да/нет): ").lower()
            if replace == 'да':
                print("Отлично!")
                break
            elif replace == 'нет':
                new_word = input("Введите слово, которое хотите добавить: ").lower()
                line = line.strip() + f", {new_word}\n"
                print("Слово успешно добавлено!")
            else:
                print("Ошибка: необходимо ввести да или нет")
                break
        f.write(line)

    if not found_word:
        print("Данного слова нет в списке")