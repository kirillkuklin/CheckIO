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
                    n = 0
                    if m > n:  # 1 > 0
                        n = m  # 0 becomes 1
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

print(max(3, 2))
print(min(3, 2))
print(max([1, 2, 0, 3, 4]))
print(min("hello"))
print(max(2.2, 5.6, 5.9, key=int))
print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))











