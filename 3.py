# Запит вводу довжин сторін прямокутника від користувача
a = float(input("Введіть довжину сторони a прямокутника: "))
b = float(input("Введіть довжину сторони b прямокутника: "))

# Обчислення площі прямокутника за формулою S=a*b
S = a * b

# Обчислення периметру прямокутника за формулою P=2*(a+b)
P = 2 * (a + b)

# Виведення результату на екран
print("Площа прямокутника зі сторонами", a, "і", b, "дорівнює", S)
print("Периметр прямокутника зі сторонами", a, "і", b, "дорівнює", P)
