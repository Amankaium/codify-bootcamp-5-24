num = int(input())

for i in range(num+2):
    if i == 0 or i == num + 1:
        print("_ " * num)
    else:
        print("|" + " " * (num + 2) + "|")
