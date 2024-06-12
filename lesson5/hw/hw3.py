data = {}  # {"Kaium": [97]}

# Ввод
for i in range(4):
    name = input("Имя: ")
    data[name] = []
    for j in range(3):
        mark = int(input("Оценка: "))  # 99
        data[name].append(mark)  # {"Kaium": [97, 99]}

print(data)
