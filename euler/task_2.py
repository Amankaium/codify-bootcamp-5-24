# Каждый следующий элемент ряда Фибоначчи получается при
# сложении двух предыдущих. Начиная с 1 и 2, первые 10
# элементов будут:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# Найдите сумму всех четных элементов ряда Фибоначчи,
# которые не превышают четыре миллиона.

def fib_list(max_num):
    lst = [1, 2]
    while True:
        num = lst[-1] + lst[-2]
        if num > max_num:
            break
        lst.append(num)
    return lst

def sum_even(lst):  # fib_100
    res = 0
    for num in lst:
        if num % 2 == 0:
            res += num
    return res

fib_100 = fib_list(100)
r = sum_even(fib_100)
print(r)  # 44

fib_4 = fib_list(4000000)
r_4 = sum_even(fib_4)
print(r_4)  # 4613732
