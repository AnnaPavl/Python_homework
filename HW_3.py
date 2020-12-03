#1
while True:
    try:
        a = float(input("Введите делимое  "))
        while True:
            try:
                b = float(input("Введите делитель  "))
                try:
                    def dell_d(a, b):
                        return a / b
                    c = round((dell_d(a, b)), 2)
                    print("Частное", c)
                    break
                except ZeroDivisionError:
                    print("Делить на 0 нельзя!")
            except ValueError:
                print("Введите действительное число!")
                continue
    except ValueError:
        print("Введите действительное число!")
    continue

#2
#a
name = str(input("Введите имя  "))
surname = str(input("Введите Фамилию  "))
year = int(input("Укажите год рождения  "))
city = str(input("Укажите город проживания  "))
email = str(input("Укажите email  "))
number = input("Укажите номер телефона  ")
def func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)
func(a=name, b=surname, c=year, d=city, e=email, f=number)

#b
def func(f, e, d, c, b, a):
    print(f"Имя: {a}, Фамилия: {b}, Год рождения: {c}, Город: {d}, email: {e}, номер телефона: {f} ")
func(a="Анна", b="Павлова", c="1990", d="Москва", e="abc@mail.ru", f="123-56-98")

#c
def func(f, e, d, c, b, a):
    print(f"Имя: {a}, Фамилия: {b}, Год рождения: {c}, Город: {d}, email: {e}, номер телефона: {f} ")
func(a=(input("Введите имя  ")), b=(input("Введите Фамилию  ")), c=(input("Укажите год рождения  ")), d=(input("Укажите город проживания  ")), e=(input("Укажите email  ")), f=input("Укажите номер телефона  "))


#3
def my_func(a, b, c):
    my_list = []
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    my_list = sorted(my_list)
    d = my_list[1] + my_list[2]
    print(my_list)
    print(d)

my_func(a = float(input("Ведите 1-ое число  ")), b = float(input("Ведите 2-ое число  ")), c = float(input("Ведите 3-е число  ")))


#4
#a
while True:
    x = float(input("Ведите 1-ое число  "))
    if x <= 0:
        print("Введите действительное положительное число  ")
        continue
    else:
        while True:
            try:
                y = int(input("Ведите 2-ое число  "))
            except ValueError:
                print("Введите целое число  ")
                continue
            if y >= 0:
                print("Введите отрицательное число  ")
                continue
            if y < 0:
                def my_func(x, y):
                    return x ** y
                c = round((my_func(x, y)), 5)
                print(c)
            break
        break

#b
def my_func():
    global x, y, z, c, m
    while True:
        try:
            x = float(input("Ведите 1-ое число  "))
        except ValueError:
            print("Введите число  ")
            continue
        if x <= 0:
            print("Введите действительное положительное число  ")
            continue
        else:
            while True:
                try:
                    y = int(input("Ведите 2-ое число  "))
                except ValueError:
                    print("Введите целое число  ")
                    continue
                if y >= 0:
                    print("Введите отрицательное число  ")
                    continue
                if y < 0:
                    break
            break
    z = 1
    m = x
    while True:
        if z != (y*(-1)):
            z += 1
            x *= m
            c = 1 / x
            continue
        else:
            break
    return c


c = round((my_func()), 5)
print(c)




#5
a = None
b = 0
z = None
while True:
    num = input("Введите числа ")
    if num.find("$") == -1:
        num = num.split()
        num_1 = list(map(int, num))
        a = sum(num_1) + b
        b = a
        print(a)
        continue
    if num.find("$") > 0:
        num = num.split()
        z = num.index("$")
        num_1 = num[:z]
        num_2 = list(map(int, num_1))
        a = sum(num_2) + b
        print(a)
        break
    if num.find("$") == 0:
        break
    break

#6
def int_func():
    global a, c, s, w, e
    s = []
    w = 1
    e = 0
    while True:
        a = input("Введите текст   ")
        c = list(map(str, a))
        while w <= len(c):
            if a.islower() == False:
                print("Введите текст прописными буквами  ")
                break
            if ord(c[e]) > 122 or ord(c[e]) < 97 and ord(c[e]) != 32:
                print("Введите текст латинскими буквами  ")
                break
            else:
                e += 1
                w += 1
                continue
        else:
            a = a.title()
            break
    return a


print(int_func())