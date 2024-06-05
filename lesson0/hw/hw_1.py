a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))

if a > b:
    if a > c:
        if a > d:
            if a > e:
                print(a)
            else:
                print(e)
        else:
            if d > e:
                print(d)
            else:
                print(e)
    else:
        if c > d:
            if c > e:
                print(c)
            else:
                print(e)
        else:
            if d > e:
                print(d)
            else:
                print(e)
else:
    if b > c:
        if b > d:
            if b > e:
                print(b)
            else:
                print(e)
        else:
            if d > e:
                print(d)
            else:
                print(e)
    else:
        if c > d:
            if c > e:
                print(c)
            else:
                print(e)
        else:
            if d > e:
                print(d)
            else:
                print(e)
