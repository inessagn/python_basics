"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time

class TrafficLight:
    __states = {'red': 7, 'yellow': 2, 'green': 8}

    def change_color(self, color):

        self.__color = color
        delay = TrafficLight.__states[color]
        print(f'{self.__color} - {delay}s')
        time.sleep(delay) 

    def running(self):
        self.change_color('red')
        self.change_color('yellow')
        self.change_color('green')

traffic_light = TrafficLight()
traffic_light.running()
