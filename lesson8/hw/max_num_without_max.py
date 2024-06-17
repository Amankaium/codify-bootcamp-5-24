def search_max_num(number):
    val = number[0]
    for v in number[1:]:  # перебираем остальные
        if val < v:
            val = v
    return val


print(search_max_num([1, 2, 3, 4, 100, 5, 6, 10, 78]))
print(search_max_num([1, 2, 3, 4, 100, 5, 6, 10, 78, 1000, 8, 3000]))