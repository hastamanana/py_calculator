# "Калькулятор" – программа для выполнения базовых арифметических операций
# (сложение, вычитание, умножение, деление).

def calc():
    opers = ['+', '-', '*', '/', '%', '^']
    try:
        a = int(input('Введите число 1: '))
        b = int(input('Введите число 2: '))
    except ValueError:
        print('Введен неверный тип данных (нужен "int")')
    oper = input("Введите операцию ('+', '-', '*', '/', '%', '^'): ")
    if oper not in opers:
        raise ValueError('Вы ввели неверную операцию')
    if oper == '+':
        return a + b
    if oper == '-':
        return a - b
    if oper == '*':
        return a * b
    if oper == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return("Ошибка: Деление на ноль!")
    if oper == '%':
        return a % b
    if oper == '^':
        return a ** b
    

print(calc())
