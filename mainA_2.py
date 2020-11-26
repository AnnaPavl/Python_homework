#1(a)
list_a = ["Hello", 30, 2.3, True, None, ("yes", "no", 4), {2.3, "ok", 8}, {"yes": 1, "no": 1}]
x = 0
while x <= (len(list_a) - 1):
    print(type(list_a[x]))
    x += 1

#1(b)
list_a = ["Hello", 30, 2.3, True, None, ("yes", "no", 4), {2.3, "ok", 8}, {"yes": 1, "no": 1}]
for ind, el in enumerate(list_a, 1):
    print(ind, type(el))


#2

count = int(input("Введите количество элементов списка "))
x = 1
list_a = []
while count >= x:
    a = input(f"Введите значение {x} элемента ")
    x += 1
    list_a.append(a)
print(list_a)
a = len(list_a)
if a % 2 == 0:
    list_a[::2], list_a[1::2] = list_a[1::2], list_a[::2]
else:
    my_list = [list_a[a - 1]]
    list_a.pop(a - 1)
    list_a[::2], list_a[1::2] = list_a[1::2], list_a[::2]
    list_a.extend(my_list)
print(list_a)

#3
m = int(input("Введите число  "))
a = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if m in a[0:3]:
    print("Зима")
elif m in a[3:6]:
    print("Весна")
elif 6 <= a.index(m) < 9:
    print("Лето")
else:
    print("Осень")

b = {1: "Зима", 2: "Зима", 12: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето"}
print(b.get(m))

#4
a = input("Введите предложение  ")
for ind, el in enumerate(a.split(), 1):
    print(ind, el[0:10])

#5
my_list = [7, 4, 3, 3, 2]
x = float(input("Введите новый элемент  "))
print(my_list, "Изначальный список")
a = my_list.count(x)
y = 0
if x > my_list[0] and a == 0:
    my_list.insert(0, x)
    print(my_list)
if x < my_list[-1] and a == 0:
    my_list.append(x)
    print(my_list)
while a == 0 and my_list[0] > x > my_list[-1]:
    if my_list[y] > x > my_list[y + 1]:
        my_list.insert(y + 1, x)
        print(my_list)
        break
    else:
        y += 1
        continue
b = my_list.index(x)
while a >= 2:
    if my_list[b:].count(x) > 1:
        b += 1
        continue
    else:
        my_list.insert(b + 1, x)
        print(my_list)
        break


#6
qw = int(input("Укажите количество позиций  "))
name_list = []
price_list = []
num_list = []
ed_list = []
dict = {"Название": name_list, "Цена": price_list, "Количество": num_list, "Единица измерения": ed_list}
list_all = []
x = 1
while x <= qw:
    name = input("Укажите название товара  ")
    name_list.append(name)
    price = int(input("Укажите цену товара  "))
    price_list.append(price)
    num = int(input("Укажите количество товара  "))
    num_list.append(num)
    ed = input("Укажите единицу измерения товара  ")
    ed_list.append(ed)
    list_all.append((x, {"Название": name, "Цена": price, "Количество": num, "Единица измерения": ed}))
    x += 1
    continue
print("Аналитика", dict)
print("Структура", list_all)