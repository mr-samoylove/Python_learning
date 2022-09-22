# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 10.01] => 0.19

mylist = [1.1, 1.2, 3.1, 10.01]
mylist = list(map(lambda num: abs(num - int(num)), mylist))

print(round(max(mylist) - min(mylist), 2))


# Было:
# mylist = [1.1, 1.2, 3.1, 10.01]
#
# for i in range(len(mylist)):
#     mylist[i] = abs(mylist[i])
#     mylist[i] -= int(mylist[i])
#
# print(round(max(mylist) - min(mylist), 2))
