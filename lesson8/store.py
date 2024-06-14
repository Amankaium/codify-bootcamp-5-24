lst = [5, 7, [8, 2], 7, 4, 9, [[[[[[[[[[6, 4, 2]]]], 7]]]]]], 8, 3, 8]

def unpack(element, res=[]): # lst
    for item in element:  # lst # item = [[[[[[[6, 4, 2]]]], 7]]]
        if isinstance(item, list):
            res = unpack(item, res)  # [5, 7, 8, 2]
            # unpack([6, 4, 2], [5, 7, 8, 2, 7, 4, 9])
        else:
            res.append(item)  # [5, 7, 8, 2, 7, 4, 9, 6, 4, 2, 7]
    return res

print(unpack(lst))
# unpack(lst) # [...]
