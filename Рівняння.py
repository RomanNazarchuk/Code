import math

# Зчитування коефіцієнтів a, b та c
a, b, c = map(int, input().split())

# Обчислення дискримінанту
discriminant = b**2 - 4*a*c

# Визначення кількості коренів
if discriminant < 0:
    print("No roots")
elif discriminant == 0:
    root = -b / (2*a)
    print("One root: {:.0f}".format(root))
else:
    root1 = (-b - math.sqrt(discriminant)) / (2*a)
    root2 = (-b + math.sqrt(discriminant)) / (2*a)
    print("Two roots: {:.0f} {:.0f}".format(min(root1, root2), max(root1, root2)))
