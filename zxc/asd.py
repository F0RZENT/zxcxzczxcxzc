import math

# Перовое задание:
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 == num2 and num2 == num3:
    print("Треугольник является равносторонним")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Треугольник является равнобедренным")
elif num1 != num2 or num2 != num3 or num1 != num3:
    print("Треугольник является разносторонним")

P = (num1 + num2 + num3) / 2
S = math.sqrt(P * (P - num1) * (P - num2) * (P - num3))
print(f"Площаль треугольника: {S}")

# Второе задание:
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 > num2 and num1 > num3:
    max = num1
    one = num2
    two = num3
elif num2 > num1 and num2 > num3:
    max = num2
    one = num1
    two = num3
elif num3 > num1 and num3 > num2:
    max = num3
    one = num1
    two = num2

if max**2 == one**2 + two**2:
    print("Треугольник явялется прямоугольным")
elif max**2 < one**2 + two**2:
    print("Треугольник является остроугольнным")
elif max**2 > one**2 + two**2:
    print("Треугольник является тупоугольником")

P = (num1 + num2 + num3) / 2
S = math.sqrt(P * (P - num1) * (P - num2) * (P - num3))
print(f"Площадь треугольника: {S}")