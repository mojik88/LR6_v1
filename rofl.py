# Задаем символы, которые будем использовать для создания рисунка
symbols = ['*', '.', '+', 'o', '#', '@']

# Создаем функцию для печати символа в нужном формате
def print_symbol(char):
    return symbols[hash(char) % len(symbols)]

# Создаем массив для букв
ascii_art = [
    "N    N III K   K FFFFF III RRRR  EEEEE",
    "NN   N  I  K  K  F      I  R   R E    ",
    "N N  N  I  KKK   FFF    I  RRRR  EEEE ",
    "N  N N  I  K  K  F      I  R  R  E    ",
    "N   NN III K   K F      III R   R EEEEE",
]

# Печатаем рисунок
for line in ascii_art:
    print("".join(print_symbol(c) if c != " " else " " for c in line))