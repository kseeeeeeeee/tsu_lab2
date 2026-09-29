def recursive_sum(n):
    if n <= 0:
        return 0

    return n + recursive_sum(n - 1)


number = int(input("Введите число: "))

result = recursive_sum(number)

print("Сумма чисел от 1 до", number, ":", result)