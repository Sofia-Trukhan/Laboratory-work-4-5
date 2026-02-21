epsilon = float(input("Введіть точність ε: "))

suma = 0
i = 1

while True:
    term = ((-1) ** i) * i / (1 + 2 ** i)
    
    if abs(term) < epsilon:
        break

    suma += term
    i += 1

print("Сума ряду =", suma)

