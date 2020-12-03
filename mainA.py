#1
name = input("Как вас зовут?")
age = int(input("Сколько вам лет?"))
age_2 = age + 2
print(f"Через 2 года {name} достигнет {age_2} лет")

#2
time = int(input("Введите время в секундах   "))
h = int(time/3600)
m = int((time - h * 3600) / 60)
s = time - (h * 3600 + m * 60)
print(f"Точное время {h} часов {m} минут {s} секунд")

#3
number = input("Ведите число")
print(int(number) + int(number + number) + int(number + number + number))


#4
number = int(input("Введите число "))
max_num = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max_num:
        max_num = number % 10
    if number > 9:
        continue
    else:
        print(max_num)
        break

#5
in_ = float(input("Сумма выручки  "))
out_ = float(input("Сумма издержек  "))
if in_ > out_:
    print(f"Прибыль составила {int(in_ - out_)} рублей")
    print(f"Рентабельность {in_/out_*100:.2f} % ")
if in_ < out_:
    print(f"Убыток составил {int(out_ - in_)} рублей")
if in_ == out_:
    print("В ноль")
emp = float(input("Укажите количество сотрудников  "))
if int(in_ - out_) > 0:
    print(f"Каждый сотрудник получит {(in_ - out_)/emp:.3f} рублей")
if int(out_ - in_) >= 0:
    print("Сотрудники ничего не получат")

#6
first = float(input("Количество км в первый день  "))
purpose = float(input("Укажите вашу цель в км  "))
x = first
d = 1
while purpose > x:
    x = x + x * 0.1
    d += 1
print(f"на {d} день спортсмен достиг результата — не менее {purpose} км")




