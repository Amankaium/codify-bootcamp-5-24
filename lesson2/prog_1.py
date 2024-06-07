# у вас есть список из 3-х
# чисел, пользователь
# вводит ещё 2 числа,
# вам нужно добавить
# их в список и вывести

nums = [5, 8, 2]
input_nums = input("enter nums: ")  # str # '7 4'
nums_list = input_nums.split()  # ['7', '4']

i = 0
while i < len(nums_list):
    nums.append(int(nums_list[i]))
    i += 1  # i = i + 1

print(nums)
# nums = nums + nums_list

# nums.append(int(nums_list[0]))
# nums.append(int(nums_list[1]))



