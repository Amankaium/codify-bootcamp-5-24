dictionary = {}

for i in range(4):
    name = input("Введите имя:")
    grade_list = []
    for grade in range(3):
        grades = int(input("Введите оценки:"))
        grade_list.append(grades)
    dictionary[name] = grade_list

print(dictionary)

