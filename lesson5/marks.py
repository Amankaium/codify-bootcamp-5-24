names = ["Beknazar", "Vlad", "Cholpon"]
marks = [88, 77, 44]

a = {}  # {"Beknazar": 88, ...}

for i in range(len(names)):  # 0
    name = names[i]  # 0 - Beknazar
    mark = marks[i]  # 0 - 88
    a[name] = mark
print(a)
