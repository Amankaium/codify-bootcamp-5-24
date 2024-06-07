n = 3
lst = [5, -7, "hello", False, n, None, 0]
print(len(lst))  # 7

# элемент списка
print(lst[3])
e = lst[0]
print(e)

# изменить значение
lst[5] = True

# добавить в список
lst.append("world")

# удаление
del lst[1]

print(lst)
print(len(lst))  # 7
print(lst[1])  # hello
