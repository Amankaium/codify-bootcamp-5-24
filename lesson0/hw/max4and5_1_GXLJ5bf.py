a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
f = int(input("Enter f: "))

""" 1) Нахождение максимального числа из 4"""

max_num = a

if b > max_num:
    max_num = b

if c > max_num:
    max_num = c

if d > max_num:
    max_num = d
print(max_num)


""" 2) Нахождение максимального числа из 5"""

max_num = a

if b > max_num:
    max_num = b

if c > max_num:
    max_num = c

if d > max_num:
    max_num = d

if f > max_num:
    max_num = f
print(f"Максимальное число: {max_num}")









# if a > b:
#     if a > g:
#         if a > c:
#             print(a)
#         else:
#             print(c)
# else:
#     if b > a:
#         if b > g:
#             if b > c:
#                 print(b)
#             else:
#                 print(c)
#     else:
#         if g > b:
#             if g > c:
#                 print(g)
#             else:
#                 print(c)






