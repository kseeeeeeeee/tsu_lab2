def create_squares(numbers):
    return {number: number ** 2 for number in numbers}


numbers = list(map(int, input("Введите числа через пробел: ").split()))

squares = create_squares(numbers)

print("Словарь квадратов:", squares)