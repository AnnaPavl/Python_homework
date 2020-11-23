#1
from sys import argv

zp, a, b, c = argv
f = list(map(float, [a, b, c]))

print("Количество часов ", f[0])
print("Ставка в час ", f[1])
print("Премия   ", f[2])
print("Зарплата", f[0] * f[1] + f[2])

#2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in my_list[1:] if el > my_list[my_list.index(el)-1]]
print(new_list)

#3
my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(my_list)


#4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

#5
from functools import reduce
new_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(a, b):
    return a * b
print(reduce(my_func, new_list))

#6
from itertools import count
from itertools import cycle
my_list = []
с = 0
for el in count(1):
    if el > 4:
        for el in cycle(my_list):
            if с > 12:
                break
            print(el)
            с += 1
    else:
        my_list.append(el)

#7
from math import factorial
from itertools import count
def func():
    global n
    n = int(input("Введите число "))
    for el in count(1):
        if el > n:
            break
        else:
            yield factorial(el)

for el in func():
    print(el)