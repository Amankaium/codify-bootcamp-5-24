space = int(input()) - 1
sign = 1
while space > -1:
        print(''*space + '*'*sign)
        sign += 4
        space -= 1
