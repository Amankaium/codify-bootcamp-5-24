def fib_list(max_num):
    lst = [1, 2]
    while True:
        num = lst[-1] + lst[-2]
        if num > max_num:
            break
        lst.append(num)
    return lst

# Найти число Фиббоначи, используя рекурсию
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return fib(n-1) + fib(n-2)

# print(fib(37))

print(fib_list(1000000000000000000)[-1])

