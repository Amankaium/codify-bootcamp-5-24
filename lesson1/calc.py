num_1 = float(input("Введите первое число: "))
action = input("Введите оператор: ")
num_2 = float(input("Введите второе число: "))

result = None
if action == "+":
    result = num_1 + num_2
elif action == "-":
    result = num_1 - num_2
elif action == "*":
    result = num_1 * num_2
else:
    result = "Неверный ввод"
print(result)
