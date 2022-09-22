# 2. Для натурального n создать последовательности 3n + 1.
# *Пример:*
# - Для n = 6:
# 1: 4,
# 2: 7,
# 3: 10,
# 4: 13,
# 5: 16,
# 6: 19

print(*[f"{num}: {3 * num + 1}" for num in range(1, int(input()) + 1)], sep='\n')

# Было:
#
# n = int(input())
# value = 1
# for i in range(1, n + 1):
#     value = 3 * i + 1
#     print(value)
