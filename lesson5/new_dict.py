a = ["Видеокарты", "Оптика", "Охлаждение"]  # list, array
b = {"name": "Vlad", "мяч": "ball", "age": 21, 55: 33, "has_laptop": True}  # dictionary

# чтение
print(a[1])  # "Оптика"
print(b["age"])  # 21

# добавление
a.append("Акустика")
b[7] = "seven"
print(b)

# изменение
a[2] = "Клавиатура"
b["мяч"] = "a ball"

# удаление
del a[-1]
del b[7]
print(b)
