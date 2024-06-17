# ввод
def my_input():
    # a*x**2 + b * x + c = 0
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    return a, b, c

# обработка
def calc(a, b, c):
    d = b ** 2 - 4 * a * c
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    return x_1, x_2

# вывод
def my_print(value):
    print(f"Результат: {value}")

def solve_quater_equasion():
    a, b, c = my_input()  # ввод
    x_1, x_2 = calc(a, b, c) # обработка
    my_print([x_1, x_2]) # отображение

# 3, -14, -5 => 5, - 1/3
# solve_quater_equasion()
