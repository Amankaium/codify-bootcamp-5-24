def first():
    print("this is first")
    return 1

def second():
    first()
    print("this is second")
    return 2

def third(fn):
    fn()
    print("third")
    first()
    return 3

# second()
# third(second)
third(first)

