m = [
    [5, 3, 0],
    [3, 9, 2],
    [7, 5, 1],
    [6, 7, 4],
]

nums = []  # [5, 3, 0, 3, 9, 2, ...]

for e in m:
    # e - это список
    for num in e:
        nums.append(num)
print(nums)

for i in range(len(m)):
    # m[i] - это список
    for j in range(len(m[i])):
        print(m[i][j])  # m[1][0] # 3
