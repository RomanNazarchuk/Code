n = int(input())

# Знаходимо цифри числа
digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10

# Знаходимо добуток цифр
product = digit1 * digit2 * digit3

print(product)
