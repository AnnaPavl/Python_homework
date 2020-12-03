#1
import time
import colorama
from colorama import Fore, Style


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            self._TrafficLight__color = input("Введите цвет ")
            if self._TrafficLight__color == "red":
                print(Fore.RED + "Красный свет: Stop!!!")
                time.sleep(7)
                print(Fore.YELLOW + "Желтый свет мигает: Остановитесь!")
                time.sleep(2)
                print(Style.RESET_ALL)
                continue
            if self.__color == "yellow":
                print(Fore.YELLOW + "Желтый свет: Ждите...")
                time.sleep(2)
                print(Style.RESET_ALL)
                continue
            if self.__color == "green":
                print(Fore.GREEN + "Зелёный свет: Идите)")
                time.sleep(5)
                print(Fore.YELLOW + "Желтый свет мигает: Остановитесь!")
                time.sleep(2)
                print(Style.RESET_ALL)
                continue
            else:
                break


r = TrafficLight()

r.running()


#2
import random


class Road:
    def __init__(self):
        self._length = random.randint(1, 50)
        self._width = random.randint(1, 30)

    def massa(self):
        b = float(input("Укажите число см толщины полотна   "))
        s = self._length * self._width * 25 * b / 1000
        print(f"Масса асфальта длиной {self._length} м и шириной {self._width} м составит {s} т")


r = Road()
r.massa()

#3
class Worker:
    def __init__(self):
        self.name = input("Введите имя ")
        self.surname = input("Введите Фамилию ")
        self.position = input("Введите должность ")
        self._income = {"wage": float(input("Укажите размер оклада ")), "bonus": float(input("Укажите размер премии "))}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.position} {self.name} {self.surname}")

    def get_total_income(self):
        b = sum([self._income.setdefault("wage"), self._income.setdefault("bonus")])
        print(f"Доход составляет {b}")
        print(self._income)


s = Position()
s.get_full_name()
s.get_total_income()

#4
from random import choice


class Car:
    def __init__(self):
        self.speed = float(input("Укажите скорость транспортного средства "))
        self.color = input("Укажите цвет автомобиля ")
        self.name = input("Введите название автомобиля ")
        self.is_police = None

    def go(self):
        print(F"{self.color} {self.name} начинает движение по городу.")

    def stop(self):
        direction = ["на севере", "на юге", "на востоке", "на западе"]
        print(f"{self.color} {self.name} прекратил движение {choice(direction)} города.")

    def turn_direction(self):
        direction = ["направо", "налево", "вперед", "назад"]
        print(f"{self.color} {self.name} двигается {choice(direction)}")

    def show_speed(self):
        print(f"Скорость {self.color}{self.name} составляет {self.speed} км/ч  - скорость в норме")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Это городская машина. Скорость превышена!!!")
        if self.speed <= 60:
            super().show_speed()


class SportCar(Car):
    def cool(self):
        print("Крутая тачка!!!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Это рабочая машина. Скорость превышена!!!")
        if self.speed <= 40:
            super().show_speed()


class PoliceCar(Car):
    def police(self):
        print("Полиция в погоне!!!")


t = TownCar()
t.go()
t.turn_direction()
t.show_speed()
t.stop()
p = PoliceCar()
p.go()
p.turn_direction()
p.show_speed()
p.police()
p.stop()
w = WorkCar()
w.go()
w.turn_direction()
w.show_speed()
w.stop()
s = SportCar()
s.go()
s.turn_direction()
s.show_speed()
s.stop()
s.cool()

#5
class Stationery:
    def __init__(self):
        self.title = input("Укажите тип канцелярской принадлежности ")

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"{self.title} начинает рисовать")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} начинает рисовать")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} начинает рисовать")

p = Pen()
p.draw()
pe = Pencil()
pe.draw()
h = Handle()
h.draw()