"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.
"""
first = 1
second = 2
third = "third"
print(first, second, third)

first = int(input('Введите любое число: '))
second = float(input('Введите любое число с "плавающей" точкой: '))
third = input('Введите любое слово: ')

print(f'Вы ввели {first}, {second}, {third}')

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""
seconds = int(input('Введите количество секунд: '))
if seconds >= 60*60:
    hours = int(seconds // (60*60))
    minutes = int(seconds % (60*60) / 60)
    seconds = seconds % 60
    print(f'Вы ввели время {hours}:{minutes}:{seconds}')
elif seconds >= 60:
    minutes = int(seconds % (60*60) / 60)
    seconds = seconds % 60
    print(f'Вы ввели время 00:{minutes}:{seconds}')
else:
    print(f'Вы ввели время 00:00:{seconds}')

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.
"""
number = input('Введите число n: ')
summa = int(number) + int(number*2) + int(number*3)
print(f'Сумма чисел n + nn + nnn равна: {summa}')


"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
"""
number = int(input('Введите целое положительное число: '))
i = number % 10
number = number // 10
while number > 0:
    if number % 10 > i:
        i = number % 10
    number = number // 10
print(i)

"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
 (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. 
 Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
 Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
proceeds = int(input('Введите значение выручки в рублях: '))
costs = int(input('Введите значение издержек в рублях: '))
profit = proceeds - costs
if profit > 0:
    profitability = profit / proceeds * 100
    print('Поздравляем, ваша прибыль {} рублей, рентабельность {:.2f}%'.format(profit, profitability))
    number_of_employees = int(input('Введите количество сотрудников: '))
    profit_for_employee = profit / number_of_employees
    print('В расчете на одного сотрудника вы имеете прибыль {:.2f} рублей'.format(profit_for_employee))
else:
    print(f'Пока вы ничего не заработали. Ваш результат / убыток {profit} рублей. Попробуйте что-то изменить.')

"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = int(input('Результат первого дня в километрах: '))
b = int(input('Цель - пробежать в километрах: '))
results = [a]
while a < b:
    a += a*0.1
    results.append(a)
days = len(results)
print(f'Потребуется {days} дней')
