#1
hw = open("lesson_5.txt", "w")
while True:
    a = input("Введите строку в файл  ")
    if len(a) > 0:
        a = f"{a}\n"
        hw.write(a)
    else:
        hw.close()
        break
print("Файл закрыт")

#2
hw = open("hw_2.txt", "r")
content = hw.readlines()
b = len(content)
print(f"В файле {b} строк(и)")
for i, el in enumerate(content):
    content[i].split()
    a = len(content[i].split())
    print(f"В {i+1} строке {a} слов(а)")
hw.close()

#3
hw = open("text_3.txt", "r", encoding="utf-8")
content = hw.readlines()
zp = []
zzp = []
sotr = []
for i, el in enumerate(content):
    f = content[i].split()
    zp.append(f[1])
    sotr.append(f[0])
    zzp = list(map(float, zp))
o = 1
s = 0
p = zzp[s]
q = 0
e = 0
while True:
    if o < len(zzp) and zzp[e] < 20000:
        print(f"{sotr[e]} имеет оклад менее 20 тыс.")
        o += 1
        e += 1
        continue
    if zzp[e] > 20000 and o < len(zzp):
        o += 1
        e += 1
        continue
    if o == len(zzp) and zzp[e] > 20000:
        o += 1
        continue
    if o == len(zzp) and zzp[e] < 20000:
        print(f"{sotr[e]} имеет оклад менее 20 тыс.")
        o += 1
        continue
    if o > len(zzp):
        while True:
            if s + 1 < len(zzp):
                q = p + zzp[s + 1]
                p = p + zzp[s + 1]
                s += 1
            else:
                e = q / len(zzp)
                print(f"Средняя величина дохода сотрудников составляет {e}")
                break
        break
hw.close()

#4
hw = open("text_4.txt", "r", encoding="utf-8")
new = open("new_4.txt", "w")
content = hw.read()
t = content.lower()
b = list(map(str, t.split()))
numb = {"one": "Один", "two": "Два", "three": "Три", "four": "Четыре"}
e = 0
while True:
    if b[e] in numb.keys() and e + 1 < len(b):
        c = numb.get(b[e])
        new.write(f"{c} ")
        e += 1
        continue
    if b[e] not in numb.keys() and e + 1 < len(b) and b[e].isdigit() == False:
        new.write(f"{b[e]} ")
        e += 1
        continue
    if b[e].isdigit() == True and e + 1 < len(b):
        new.write(f"{b[e]}\n")
        e += 1
        continue
    if b[e].isdigit() == True and e + 1 == len(b):
        new.write(f"{b[e]}\n")
        break
new.close()
hw.close()

#5
hw = open("lesson_7.txt", "w")
list = "1   56   96   85"
hw.write(list)
hw = open("lesson_7.txt", "r")
content = hw.readlines()
num = str(content[0])
num_2 = num.split()
e = 1
t = 0
c = int(num_2[t])
while True:
    if e < len(num_2):
        d = c + int(num_2 [t + 1])
        c = c + int(num_2 [t + 1])
        e += 1
        t += 1
        continue
    if e >= len(num_2):
        print(d)
        break
hw.close()

#6
hw = open("text_6.txt", "r", encoding="utf-8")
content = hw.readlines()
s = 0
h = 1
dict = {}
while True:
    if h <= len(content):
        c = content[s].replace("(", " ").replace(":", " ").split()
        e = 0
        a = 1
        k = 0
        while True:
            if a < len(c) and c[e].isdigit() == True:
                d = int(c[e]) + k
                k = d
                a += 1
                e += 1
                continue
            if a < len(c) and c[e].isdigit() == False:
                a += 1
                e += 1
                continue
            if a == len(c) and c[e].isdigit() == False:
                dict.update({c[0]: k})
                s += 1
                h += 1
                break
            if a == len(c) and c[e].isdigit() == True:
                d = int(c[e]) + k
                k = d
                dict.update({c[0]: k})
                s += 1
                h += 1
                break
    if h > len(content):
        print(dict)
        break
hw.close()


#7
with open("text_7.txt", encoding="utf-8") as file:
    dict_1 = {}
    dict_2 = {}
    list = []
    k = 0
    g = 0
    for line in file:
        line_1 = line.split()
        c = int(line_1[-2])
        d = int(line_1[-1])
        a = c - d
        dict_1.update({line_1[0]: a})
        if a > 0:
            list.append(a)
            f = a + k
            k = f
            g = k/len(list)
total = [dict_1, {"average_profit": g}]
import json
with open("my_file.json", "w", encoding="utf-8") as write_f:
    json.dump(total, write_f, ensure_ascii=False, sort_keys=True, indent=4)