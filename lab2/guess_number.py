import random


secret_number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100.")

while True:
    guess = int(input("Попробуйте угадать число: "))
    attempts += 1

    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
        break