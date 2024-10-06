import random


def guess_the_number():
    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Привет! Я загадал число от 1 до 100.")
    print("Попробуй угадать его!")

    while True:
        try:
            # Получаем число от пользователя
            guess = int(input("Введите ваше предположение: "))
            attempts += 1

            # Проверяем угадал ли пользователь
            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")


# Запускаем игру
guess_the_number()
