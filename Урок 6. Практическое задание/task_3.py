"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = { "wage": wage, "bonus": bonus }

class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'
    
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]
    
    def __str__(self):
        return f'{self.position} {self.get_full_name()}, полный заработок: {self.get_total_income()} р. в месяц'
    
employee = Position("Василий", "Петров", "Бухгалтер", 20_000, 5_000)
print(f'Информация о сотруднике: {employee}')