# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Эта программа по заданному номеру четверти показывает диапазон возможных координат точек (x и y)')

chart = int(input())

if chart in [1, 4]:  # assess x
    print('x > 0')
else:
    print('x < 0')

if chart in [1, 2]:  # assess y
    print('y > 0')
else:
    print('y < 0')