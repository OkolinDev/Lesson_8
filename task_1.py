# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.


class Data:
    def __init__(self, all_data):
        self.all_data = str(all_data)

    @classmethod
    def extraction(cls, all_data):
        dati = []

        for i in all_data.split():
            if i != '-':
                dati.append(i)
        return int(dati[0]), int (dati[1]), int(dati[2])

    def __str__(self):
        return f'Сегодняшняя дата: {Data.extraction(self.all_data)}'

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Сегодняшняя дата'
                else:
                    return f'неправильный год'
            else:
                return f'неправильный месяц'
        else:
            return f'неправильный день'




day1 = Data('01 - 01  - 2021')
print(day1)
print(day1.valid(11, 13, 2021))
print(day1.valid(11, 12, 2022))
print(day1.valid(32, 12, 2022))
print(Data.extraction('01 - 01  - 2021'))
