n = int(input())
naj_goliamo = int(input())

for i in range(n - 1):
    chislo = int(input())
    if chislo > naj_goliamo:
        naj_goliamo = chislo
print(naj_goliamo)

suma = 0

for i in range(n):
    chislo = int(input())
    suma = suma + chislo

print(suma)

for i in range(1, n + 1):
    print("*" * i)