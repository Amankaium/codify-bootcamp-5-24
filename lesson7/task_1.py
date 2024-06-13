data = [
    [5, 7, 2, 8],  # [5, 7, 2, 8, 22]
    [2, 4, 6, 9],
    [1, 3, 7, 0],
] # [8, 14, 15, 17]
sm = [0, 0, 0, 0]

for i in range(len(data)):  # 0, 1, 2
    for j in range(len(data[0])):  # 0, 1, 2, 3
        sm[j] += data[i][j]
print(sm)
data.append(sm)
print(data)
for row in data:
    res = sum(row)
    row.append(res)
print(data)


