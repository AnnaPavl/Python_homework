#1
class Data:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"{self.date[0:2]}-{self.date[3:5]}-{self.date[6:10]}, {type(self.date[1])}"

    @classmethod
    def type_int(cls, date):
        day, month, year = list(map(int, date.split("-")))
        return f"{day}-{month}-{year}, {type(day)}"

    @staticmethod
    def valid(date):
        date = list(map(int, date.split("-")))
        while True:
            if date[0] < 0 or date[0] > 31:
                return f"Такого дня не существует"
            if date[1] < 0 or date[1] > 12:
                return f"Такого месяца не существует"
            if date[2] < 0 or date[2] > 9999:
                return f"Такого года не существует"
            else:
                return f"Дата указана корректно: {date[0]}-{date[1]}-{date[2]}"


a = Data("04-12-2020")
print(a)
print(Data.type_int(a.date))
a.type_int("13-09-2013")
a.valid("13-09-2013")
print(Data.valid("12-05-2013"))

#2
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = float(input("Введите делимое: "))
b = float(input("Введите делитель: "))

try:
    if b == 0:
        raise OwnError("На нуль делить нельзя!!!")
except OwnError as err:
    print(err)
else:
    print(a / b)

#3
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


b = []
while True:
    a = input("Введите либо элемент списка, либо Q для завершения работы: ")
    if a.isdigit() == False:
        try:
            if a.lower() == "q":
                print(f"Итоговый список: {b}")
                break
            else:
                raise OwnError("Можно добавлять только числа!!! Элемент не добавлен в список!!!")
        except OwnError as err:
            print(err)
            continue
    if a.isdigit() == True:
        b.append(a)
        print("Элемент добавлен в список!")
        continue

#4
from abc import ABC, abstractmethod


class Sclad:
    def __init__(self):
        self.total = {}


class Org:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def dob(self):
        pass


class Print(Org):
    def __init__(self, name, count, price, color):
        super().__init__(name)
        self.color = bool(color)
        self.count = count
        self.price = price
        self.voc = {}

    def dob(self):
        self.voc.update({self.name: self.count})
        return f"Товар {self.voc} добавлен"


class Scan(Org):
    def __init__(self, name, count, price, new):
        super().__init__(name)
        self.new = bool(new)
        self.count = count
        self.price = price
        self.voc = {}

    def dob(self):
        self.voc.update({self.name: self.count})
        return f"Товар {self.voc} добавлен"


class Xser(Org):
    def __init__(self, name, count, price, sony):
        super().__init__(name)
        self.sony = bool(sony)
        self.count = count
        self.price = price
        self.voc = {}

    def dob(self):
        self.voc.update({self.name: self.count})
        return f"Товар {self.voc} добавлен"


p = Print("Принтер", 3, 253, True)
s = Scan("Сканер", 4, 400, False)
x = Xser("Ксерокс", 6, 158, True)
print(p.dob())
print(s.dob())
print(x.dob())


#5
class Compleks:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        self.number = self.number.replace("+", " ").replace("j", " ").split()
        b = list(map(int, self.number))
        other.number = other.number.replace("+", " ").replace("j", " ").split()
        c = list(map(int, other.number))
        return f"{b[0] + c[0]}+{b[1] + c[1]}j"


    def __mul__(self, other):
        b = list(map(int, self.number))
        c = list(map(int, other.number))
        return f"{b[0]*c[0] + b[1]  * c[1] *(-1)}+{b[0] * c[1] + b[1]  * c[0]}j"


a = Compleks("1+2j")
b = Compleks("3+4j")
print(a.number)
print(a + b)
print(a * b)