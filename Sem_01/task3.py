# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Эта программа принимает на вход координаты точки (X и Y, X ≠ 0 и Y ≠ 0), и выдаёт номер четверти плоскости,")
x, y = int(input()), int(input())

if x > 0 and y > 0:
    print("1, Сверху справа")
elif x > 0 and y < 0:
    print("4, Снизу справа")
elif x < 0 and y < 0:
    print("3, Снизу слева")
else:
    print("2, Сверху слева")