def sum_cifr(a):
    b = str(a)
    d = []
    for i in range(len(b)):
        d.append(int(b[i]))
    s = sum(d)
    return s

print(sum_cifr(2**1000))
