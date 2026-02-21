import math

N = int(input("Введіть N: "))

suma = 0

for i in range(1, N + 1):
    suma += (i + 1) / math.factorial(i)

print("Сума =", suma)
