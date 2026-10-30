import random
#zad 1
a1 = int(input("enter something"))
b1 = []
for i in range(a1):
    b1.append(random.randint(1,10))
print(b1)
print(b1[:-1])
#zad 2
a2 = [random.randint(1, 20) for i in range(10)]
print("Първоначален списък:", a2)
b2 =[]
nov_b = []
for i2 in range(len(a2) - 1):
    tektusht = b2[i2]
    sledvast = b2[i2 +1]
    suma = tektusht + sledvast
    nov_b.append(tektusht)
    nov_b.append(suma)
if len(b2) > 0:
    nov_b.append(b2[-1])
b2 = nov_b

print("Нов списък:", b2)
#zad 3
text = input()
dic = {}
for char in text:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1
print(dic)
#zad 4
n4 = int(input("Въведете положително число n: "))

a4 = list(range(1, n4 + 1))
d4 = {}

for i4 in range(n4):
    d4[a4[i4]] = a4[n4 - 1 - i4]

print("Списък:", a4)
print("Речник:", d4)
#zad 5
a5 = list(map(int, input("Въведете числа: ").split()))

mn = min(a5)
mx = max(a5)

print("Най-малък елемент:", mn)
print("Брой срещания:", a5.count(mn))

print("Най-голям елемент:", mx)
print("Брой срещания:", a5.count(mx))
#zad6
a6 = [random.randint(1, 10) for i in range(10)]
b6 = []

for x6 in a6:
    if x6 not in b6:
        b6.append(x6)

print("Първоначален списък:", a6)
print("Списък без повторения:", b6)

#zad7
a7 = list(map(int, input("Въведете числа: ").split()))
x7 = int(input("Въведете число x: "))

indeksi = []

for i7 in range(len(a7)):
    if a7[i7] == x7:
        indeksi.append(i7)

if len(indeksi) > 0:
    print("Индексите са:", indeksi)
else:
    print("Числото не се среща в списъка.")

# zad 8
a8 = list(map(int, input("Първи списък: ").split()))
b8 = list(map(int, input("Втори списък: ").split()))

c8 = []

for x8 in a8:
    if x8 in b8 and x8 not in c8:
        c8.append(x8)

print("Общи елементи:", c8)

# zad 9
a9 = tuple(map(int, input("Въведете числа: ").split()))

s9 = sum(a9)
sr = s9 / len(a9)

chetni = []

for x9 in a9:
    if x9 % 2 == 0:
        chetni.append(x9)

print("Сума:", s9)
print("Средно аритметично:", sr)
print("Кортеж с четните числа:", tuple(chetni))
# zad 10
tekst = input("Въведете изречение: ").lower()

dumi = tekst.split()
d10 = {}

for x10 in dumi:
    if x10 in d10:
        d10[x10] += 1
    else:
        d10[x10] = 1

print(d10)
# zad 11
studenti = {
    "Иван": 5.50,
    "Мария": 6.00,
    "Петър": 4.00,
    "Анна": 5.00,
    "Георги": 3.50
}

suma = 0

print("Студенти с оценка над 4.50:")

for ime in studenti:
    suma += studenti[ime]

    if studenti[ime] > 4.50:
        print(ime)

sredno = suma / len(studenti)

print("Среден успех:", sredno)
# zad 12
a12 = {"Ябълки": 10, "Круши": 5, "Банани": 8}
b12 = {"Ябълки": 7, "Банани": 4, "Портокали": 6}

c12 = a12.copy()

for produkt in b12:
    if produkt in c12:
        c12[produkt] += b12[produkt]
    else:
        c12[produkt] = b12[produkt]

print("Обединен речник:", c12)
# zad 13
a13 = set(map(int, input("Въведете първото множество: ").split()))
b13 = set(map(int, input("Въведете второто множество: ").split()))

print("Обединение:", a13 | b13)
print("Сечение:", a13 & b13)
print("Разлика:", a13 - b13)
print("Симетрична разлика:", a13 ^ b13)
# zad 14
a14 = list(map(int, input("Въведете числа: ").split()))

m14 = set(a14)

print("Уникални числа:", m14)
print("Брой различни числа:", len(m14))

print("Числа, които се повтарят:")

for x14 in m14:
    if a14.count(x14) > 1:
        print(x14)
# zad 15
n15 = int(input("Въведете n: "))

d15 = {}

for i15 in range(1, n15 + 1):
    d15[i15] = (i15 ** 2, i15 ** 3)

print(d15)