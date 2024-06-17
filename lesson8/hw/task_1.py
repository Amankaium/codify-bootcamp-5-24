def search_max_num(lst):
    dragon = lst[0]
    for num in lst:
        if num > dragon:  # 5 > 100
            dragon = num
    return dragon


print(search_max_num([1, 2, 3, 4, 100, 5, 6, 10, 78]))
print(search_max_num([-5, -3, -8]))
