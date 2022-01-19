"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert(cls, date):
        day, month, year = date.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def validate_date(date_inp):
        try:
            day, month, year = date_inp
            if year not in range(0, 10000):
                raise ValueError("Год введен некорректно")
            elif month not in range(1, 13):
                raise ValueError("Столько месяцев не бывает")
            elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day not in range(1, 32):
                    raise ValueError("В этом месяце нет столько дней")
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day not in range(1, 31):
                    raise ValueError("В этом месяце нет столько дней")
            elif month == 2:
                if day not in range(1, 29):
                    raise ValueError("В этом месяце нет столько дней")
        except ValueError as err:
            print(err)
        else:
            print("Дата введена корректно")


date1 = Date('31-12-7896')
my_date = date1.convert(date1.date)
print(date1.validate_date(my_date))

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту 
ситуацию и не завершиться с ошибкой.
"""


class ZeroErr(Exception):
    def __init__(self, text):
        self.text = text


a = int(input("введите число а: "))
b = int(input("введите число b: "))

try:
    b
    if b == 0:
        raise ZeroErr("Делить на 0 запрещено!")
except ZeroErr as err:
    print(err)
else:
    print(f"результат {a / b}")

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить 
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение 
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу 
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем 
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.
"""


class ValueErr(Exception):
    def __init__(self, text):
        self.text = text

user_list = []
while True:
    user_data = input('Введите числo. Для остановки введите stop: ')
    try:
        user_data
        if user_data == "stop":
            break
        elif not user_data.isdigit():
            raise ValueErr("Это не число")
        else:
            user_list.append(user_data)
    except ValueErr as err:
        print(err)
        continue
print(user_list)

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в 
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других 
данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, 
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных 
на уроках по ООП.
"""

# Честно говоря не разобралась пока. Не хочется списывать. Я сделаю позже для себя. Извиняюсь

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) 
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real1, real2, imaginary):
        self.real1 = real1
        self.real2 = real2
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real1 + other.real1 + (self.real2 + other.real2) * self.imaginary)

    def __mul__(self, other):
        return Complex(self.real1 * other.real1 + self.real2 * other.real1 * self.imaginary + self.real1 * other.real2 *
                       self.imaginary + self.real2 * other.real2 * self.imaginary ** 2)

    def __str__(self):
        return f'{self.real1} + {self.real2} * {self.imaginary}'


complex1 = Complex(2, 4, 1)

complex2 = Complex(1, 1, 1)

print(complex1)
print(complex2)

print(complex1 + complex2)
# НЕ понимаю, почему не работает сумма - где я ошиблась?