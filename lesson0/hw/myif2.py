a = int(input("vvedite chislo a: "))
b = int(input("vvedite chislo b: "))
c = int(input("vvedite chislo c: "))
d = int(input("vvedite chislo d: "))
e = int(input("vvedite chislo e: "))

if a > b and a > c and a > d and a > e:
    print(a)
if b > a and b > c and b > d and b > e:
    print(b)
if c > d and c > a and c > b and c > e:
    print(c)
if d > e and d > a and d > b and d > c:
    print(d)
else:
    print(e)









