import math  # підключення модуля для математичних операцій

# Запит введення довжини катетів від користувача
a = float(input("Введіть довжину катета a: "))
b = float(input("Введіть довжину катета b: "))

# Обчислення гіпотенузи
c = math.sqrt(a**2 + b**2)

# Обчислення периметра
p = a + b + c

# Виведення результатів на екран
print("Гіпотенуза:", c)
print("Периметр:", p)
