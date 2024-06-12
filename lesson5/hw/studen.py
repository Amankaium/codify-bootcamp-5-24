a = {}
for i in range(4):
    names = input("Vvedite name: ")
    b = []
    for k in range(3):
        marks = int(input("Vvedite mark: "))
        b.append(marks)
    a[names] = b
print(a)