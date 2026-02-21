N = int(input("Введіть N (2≤N≤30): "))
M = int(input("Введіть M (2≤M≤30): "))

count = 1  # Починаємо рахувати числа з 1

for i in range(N):
    for j in range(M):
        if j % 2 == 0:  # На парних колонках вставляємо числа
            print(count, end=" ")
            count += 1
        else:           # На непарних колонках ставимо 0
            print(0, end=" ")
    print()
