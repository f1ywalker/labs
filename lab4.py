def z1():
    def del_na_3(num):
        if num % 3 == 0:
            return True
        else:
            return False

def z2():
    def del_na_100(number):
        return 100 / number

    try:
        number = int(input("Введите число: "))
        result = del_na_100(number)
        print("Результат: ", result)
    except ValueError:
        print("Ошибка: введено не число!")
    except ZeroDivisionError:
        print("Ошибка: деление на 0!")
def z3():
    def magic_date(date_str):
        day, month, year = map(int, date_str.split('.'))
        if day * month == year % 100:
            return True
        else:
            return False
def z4():
    def is_lucky(ticket_number):
        n = len(ticket_number)
        if n % 2 != 0:
            return False

        left_half = ticket_number[:n // 2]
        right_half = ticket_number[n // 2:]

        left_sum = sum(int(ch) for ch in left_half)
        right_sum = sum(int(ch) for ch in right_half)

        return left_sum == right_sum

z1(), z2(), z3(), z4()