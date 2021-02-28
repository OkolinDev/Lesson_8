# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class DeviderByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def bynull():
        divider = int(input('Введите делимое целое число: '))
        denominator = int(input('Введите делитель целое число: '))
        try:
            return f'Результат деления = {divider/denominator}'
        except:
            return "Деление на нуль недопустимо"


print(DeviderByNull.bynull())
