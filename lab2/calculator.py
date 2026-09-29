def calculate(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second == 0:
            return "Ошибка: деление на ноль"
        return first / second
    else:
        return "Ошибка: неизвестная операция"


first = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ")
second = float(input("Введите второе число: "))

result = calculate(first, second, operation)
print("Результат:", result)