import math


def gcd(a, b):
    return math.gcd(a, b)


first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

print("НОД:", gcd(first, second))