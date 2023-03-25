"""
Задание 2.

Написать функцию для перевода доллара в евро c округлением до 2х знаков после запятой, 
если известно, что текущий курс составляет 1.17 долларов за один евро.
"""

def convert_dollar_to_euro(dollar, rate_euro_to_dollar):
    rate_dollar_to_euro = 1 / rate_euro_to_dollar
    return round(dollar * rate_dollar_to_euro, 2)

sum_in_dollar = int(input("Введите сумму в долларах:"))
sum_in_euro = convert_dollar_to_euro(sum_in_dollar, 1.17)
print(f'Сумма в евро равна {sum_in_euro}')