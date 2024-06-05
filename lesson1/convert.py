a = 7
print(a, type(a))
b = str(a)  # '7'
print(b, type(b))
# a = str(a)  # v
# print(a, type(a))
a = a + 5
print(a)

b = b + " is my number"
print(b)
c = b * 3
print(c)

if b:
    print("Hello world from b var!")

d = '9.7'
# k = int(d)  # error
m = float(d)
k = int(m)
print(m, k)

print(bool(7))  # True
print(bool(0.000001))  # True
print(bool(-8))  # True
print(bool(0))  # False

print(bool("Hello"))  # True
print(bool(" "))  # True
print(bool("\n"))  # True
print(bool(""))  # False

p = None
print(p, type(p))
print(bool(p))
