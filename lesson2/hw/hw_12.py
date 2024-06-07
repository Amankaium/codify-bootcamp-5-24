# Пользователь вводит 10 чисел.
# Вам необходимо распределить на 2 списка:
# положительные и отрицательные (учесть 0).
# Используйте цикл while, список и continue

positive = []
negative = []
i = 0

while i < 10:
    i += 1
    num = int(input("Введите число: "))

    if num == 0:
        continue

    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

print(positive)
print(negative)
