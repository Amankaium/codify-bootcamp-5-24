lst = [6, 3, 8, 3, 6, 9, 5]
# Найти количество уникальный значений
# v1
my_set = set(lst)
print(my_set)
print(len(my_set))
# v2
unique = []
for num in lst:
    if num not in unique:
        unique.append(num)
print(unique)
