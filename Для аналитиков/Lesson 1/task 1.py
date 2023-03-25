"""
Задание 1.
Написать цикл для выведения на экран каждой буквы своего ФИО.
"""

name = input('Введите ваше ФИО: ')

print('Вариант 1')
for i in range (0, len(name)):
    print(name[i])

print()
print('Вариант 2')
for symbol in name:
    print(symbol)

