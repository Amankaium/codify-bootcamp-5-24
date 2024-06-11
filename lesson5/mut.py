a = 7
b = a
a = 9
print(b)  # 7

nums = [6, 4, 1]   # [7, 4, 1]  <--- nums
lst = nums         #    ^-- lst
lst[0] = 7
print(lst)  # [7, 4, 1]
print(nums)  # [7, 4, 1]
