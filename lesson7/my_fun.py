def say_hello():
    print("hello")

def say_something(word):
    print(word)

def say_3_times(word):
    qty = 3
    print(word * qty)

def mult_5(num):
    res = num * 5
    return res

def power(k, l):
    r = k ** l
    print(r)
    return r

say_hello()
say_something("Python")
say_3_times("bla ")

b = mult_5(7)
c = b + 77
print(b)

message = say_3_times("one ")
print(message)

power(4, 3)
