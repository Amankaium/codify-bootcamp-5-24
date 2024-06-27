nums = [5, 6, 0, 4, 1]

# nums_2 = []
# for num in nums:
#     nums_2.append(str(num))

# nums_3 = [str(n) for n in nums]
# nums_4 = [n * 2 for n in nums]
# nums_5 = [n - 3 for n in nums]

# print(nums_2)
# print(nums_3)
# print(nums_4)
# print(nums_5)

nums = [5, 6, 0, 4, 1]

nums_2 = []
for num in nums:
    if num > 3:
        nums_2.append(str(num))
print(nums_2)

nums_3 = [str(n) for n in nums if n > 3]
print(nums_3)
