# Запит вводу довжин ребер прямокутного паралелепіпеда від користувача
a = float(input("Введіть довжину ребра a: "))
b = float(input("Введіть довжину ребра b: "))
c = float(input("Введіть довжину ребра c: "))

# Обчислення об'єму прямокутного паралелепіпеда за формулою V=a*b*c
V = a * b * c

# Обчислення площі поверхні прямокутного паралелепіпеда за формулою S=2*(a*b + b*c + a*c)
S = 2 * (a * b + b * c + a * c)

# Виведення результату на екран
print("Об'єм прямокутного паралелепіпеда з ребрами довжинами", a, ",", b, "та", c, "дорівнює", V)
print("Площа поверхні прямокутного паралелепіпеда з ребрами довжинами", a, ",", b, "та", c, "дорівнює", S)