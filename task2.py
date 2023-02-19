"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        number1 = int(input('Введите 1 число: '))
        number2 = int(input('Введите 2 число: '))
        if number2 == 0:
            raise MyZeroError("Делить на ноль нельзя!")
        else:
            res = number1 / number2
            return res
    except ValueError:
        return "Вы ввели не число"
    except MyZeroError as er:
        return er


print(division())
