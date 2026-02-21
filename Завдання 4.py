a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть крок h: "))

x = a
count = 0

while x <= b:
    y = x*x + 7*x + 10
    print("x =", x, "y =", y)
    
    if y == 0:
        count += 1
        
    if count == 2:
        print("Отримано два нулі.")
        break
        
    x = x + h
