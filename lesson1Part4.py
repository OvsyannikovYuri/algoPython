# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import random

lower_board = int(input("введите целое число, нижнюю границу диапазона"))
upper_board = int(input("введите целое число, верхнюю границу диапазона"))

integer_rand = random.randint(lower_board,upper_board)
print(integer_rand)

float_rand = random.uniform(lower_board,upper_board)
print(float_rand)


print(chr(abs(integer_rand)))# случайный символ на основе случайного целого