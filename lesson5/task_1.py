# у вас есть пустой словарь,
# пользователь вводит имя и возраст,
# необходимо сохранить их в словаре

profiles = []

for i in range(5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    profile = {}
    profile["name"] = name
    profile["age"] = age
    profiles.append(profile)

print(profiles)
