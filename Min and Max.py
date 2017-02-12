def max(*args, **kwargs):
    key = kwargs.get('key',)
    if key == None:
        for i in args:
            n = 0
            if type(i) == int or type(i) == float:
                for i in args:
                    if i > n:
                        n = i
                return n
            elif type(i) == list:
                for m in i:
                    # n = 0
                    if m > n:
                        n = m
                return m
    else:
        for k, v in kwargs.items():
            for i in args:
                n = 0
                if type(i) == int or type(i) == float:
                    for i in args:
                        if key(i) > n:
                            n = i
                    return n

def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        args = args[0]
        low = None
        for d in args:
            if low == None or key(d) < key(low):
                low = d
        return low
    else:
        for i in args:
            if type(i) == int or type(i) == float:
                low = args[0]
                for i in args:
                    if i < low:
                        low = i
                return low
            elif type(i) == str:
                low = ord(i[0])
                for m in i:
                    if ord(m) < low:
                        low = ord(m)
                return chr(low)
            # elif type(i) == list:
            #     low = i[0]
            #     for d in i:
            #         if d < low:
            #             low = d
            #     return low

print(max(3, 2,6, 646))
print(min(3, 2))
print(max([1, 2, 0, 3, 4]))
print(min("hello"))
print(max(2.2, 5.6, 5.9, key=int))
print(min([[1, 2], [3, 0], [9, 12]], key=lambda x: x[1]))