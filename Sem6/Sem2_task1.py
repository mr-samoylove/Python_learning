# 1. Напишите программу, которая принимает на вход число N и  выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

print([(-3) ** num for num in range(int(input()))])

# было:
#
# n = int(input())
#
# value = 1
# for _ in range(n):
#     print(value, end=' ')
#     value *= -3
