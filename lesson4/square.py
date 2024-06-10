# Пользователь вводит число,
# надо вывести квадрат такого-же размера
# Ввод: 3
# Вывод:
###
###
###
num = int(input())

# v1
for i in range(num):
    for j in range(num):
        print("* ", end='')
    print()

# v2
for k in range(num):
    print("# " * num)
