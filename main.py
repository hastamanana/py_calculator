from typing import Callable


def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y


def multi(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> float:
    if y == 0:
        raise ZeroDivisionError('Деление на ноль!')

    return x / y


def power(base: int, exp: int) -> int:
    return base ** exp


def mod(x: int, y: int) -> int | float:
    if y == 0:
        raise ZeroDivisionError('Деление на ноль!')

    return x % y


def calc(a: int, b: int, oper: str) -> float | int | str:
    callbacks: dict[str, Callable] = {
        '+': lambda x, y: x + y,
        '-': sub,
        '*': multi,
        '/': div,
        '^': power,
        '%': mod,
    }

    func: Callable = callbacks.get(oper)

    return func(a, b)


def run() -> None:
    available_operations: list[str] = ['+', '-', '*', '/', '%', '^']

    try:
        a: int = int(input('Введите число 1: '))
        b: int = int(input('Введите число 2: '))
        oper: str = input(f'Введите операцию {available_operations}: ')

        if oper not in available_operations:
            print(
                'Вы ввели неверную операцию, '
                f'список доступных операций {available_operations}'
            )

        print(calc(a, b, oper))

    except ValueError:
        print('[Ошибка]: Введен неверный тип, введите целое число')
    except ZeroDivisionError as err_msg:
        print(f'[Ошибка]: {err_msg}')
        return None


if __name__ == '__main__':
    run()
