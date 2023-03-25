"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

from abc import ABC
from abc import abstractmethod

class Base(ABC):

    @property
    @abstractmethod
    def get_volume(self):
        ...

class Clothes(Base):
    
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def get_volume(self):
        coat_rate = self.v / 6.5 + 0.5
        costume_rate = 2 * self.h + 0.3
        total_rate = coat_rate + costume_rate
        print(f'Расход ткани на пальто = {coat_rate}')
        print(f'Расход ткани на костюм = {costume_rate}')
        print(f'Общий расход ткани = {total_rate}')
        return total_rate

clothes = Clothes(12, 5)
print(clothes.get_volume)
