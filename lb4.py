import random 
#zad 1
n =int(input())
b= []
for i in range (n):
    b.append(random.randint(1,10))
print(b)
print(b[:--1])
#zad2
for i in range(n):
    b.append(random.randint(1,10))
print("оригиналния спидък ",b
nov_b =[]
for i in range(len(b)-1):
    tektusht = b[i]
    sledvasht = b[i + 1]
    suma = tektusht + sledvasht
    nov_b.append(tektusht)
    nov_b.append(suma)
    
if len(b)>0:
    nov_b.append(b[-1])
    b=nov_b
    
print(" новия списък", b)
#zad3
text = input("Въведете текст: ")

dictionary = {}

for char in text:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

print(dictionary)
