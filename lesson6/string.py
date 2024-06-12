# f
a = 6
b = 7
print("Наше число равно " + str(a))
print(f"Наше число равно {a + 6}")
print(f"Наши числа: {a} и {b}")
c = "Наши числа: {} и {}".format(a, b)
print(c)
print("Наши числа: {1} и {0}".format(a, b))
print("Наши числа: {m} и {n}".format(m=5, n=3))
print("Наши переменные: %s и %d" % ("Hello", 4))

print(len("hello world!"))  # 12
k = "hello"
l = k.replace("l", "L")
print(l)
print(k.find("L"))  # 2
print("34534".isdigit())  # True
print(k.isalpha())  # True
print("hello world".isalpha())  # False
print(k.upper())  # HELLO

names = ["Vlad", "Amantur", "Daniel"]
names_str = "".join(names)
print(names_str)
print(ord("h"))
print("hello world! hello".count(" "))
