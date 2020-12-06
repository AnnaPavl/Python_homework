#1
class Matrix:
    def __init__(self, p_1, p_2, p_3):
        self.p_1 = p_1
        self.p_2 = p_2
        self.p_3 = p_3

    def __str__(self):
        return f"{self.p_1[0]} {self.p_1[1]}\n{self.p_2[0]} {self.p_2[1]}\n{self.p_3[0]} {self.p_3[1]}"

    def __add__(self, other):
        return Matrix((self.p_1[0] + other.p_1[0], self.p_1[1] + other.p_1[1]),
                      (self.p_2[0] + other.p_2[0], self.p_2[1] + other.p_2[1]),
                      (self.p_3[0] + other.p_3[0], self.p_3[1] + other.p_3[1]))


m_1 = Matrix([31, 32], [37, 43], [51, 86])
m_2 = Matrix([5, 3], [1, 4], [7, 2])
print(m_1.p_1, m_1.p_2, m_1.p_3)
print()
print(m_2.p_1, m_2.p_2, m_2.p_3)
print()
print(m_1)
print()
print(m_2)
print()
print(m_1 + m_2)


#2
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def total(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 52:
            self.__size = 44
            print("Вы слишком толстый, ваш размер был изменён на 44.")
        else:
            self.__size = size

    @property
    def total(self):
        self.result_1 = self.size / 6.5 + 0.5
        return f"На пошив {self.name} {self.size} размера необходимо {round(self.result_1, 3)} метров ткани."


class Costume(Clothes):
    def __init__(self, name, rost):
        super().__init__(name)
        self.rost = rost

    @property
    def rost(self):
        return self.__rost

    @rost.setter
    def rost(self, rost):
        if rost > 2:
            self.__rost = rost
            print("Вы слишком высокий, костюм обойдётся Вам очень дорого")
        else:
            self.__rost = rost

    @property
    def total(self):
        self.result_2 = 2 * self.rost + 0.3
        return f"На пошив {(self.name).lower()}а на рост {self.rost} метра необходимо {round(self.result_2, 3)} метров ткани."


coat = Coat("пальто", 42)
costume = Costume("Костюм", 3)
print(coat.total)
print(costume.total)
print(f"Общий расход ткани составит: {round(coat.result_1 + costume.result_2, 3)} метра")

#3

class me:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count > other.count:
            return self.count - other.count
        else:
            return "Отрицательное значение"

    def __mul__(self, other):
        self.b = self.count * other.count
        return self.b

    def __truediv__(self, other):
        return round(self.count / other.count)

    def __floordiv__(self, other):
        return self.count // other.count

    def make_order(self, raw):
        self.raw = raw
        r = self.count // raw
        q = self.count % raw
        for i in range(1, r + 1):
            print("*" * raw)
        print("*" * q)


a = me(21)
b = me(44)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
a.make_order(6)
print()
b.make_order(8)
