def max(*args, **kwargs):
    key = kwargs.get('key', lambda x: x)
    # print("length of args:", len(args))
    if len(args) == 1:
        args = args[0]
        for i in args:
            # print(i)
            n = 0
            if type(i) == int or type(i) == float:
                for i in args:
                    if i > n:
                        n = i
                return n
            elif type(i) == list:
                for m in i:
                    if m > n:
                        n = m
                return m
    else:
        for i in args:
            # print(i)
            n = None
            # print(key(i))
            if n == None or i > n:
                # i = key(i)
                # i = n
                n = key(i)
                # n = (key(n))
        return n, i

def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    # print(len(args))
    if len(args) == 1:
        args = args[0]
        # print(args)
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

print(max(range(22)))
# print(min(3, 2))
# print(max([1, 2, 222, 3, 4]))
# print(min("hello"))
print(max(2.2, 5.6, 5.9, key=int))
# print(min([[1, 1], [3, 12], [9, 0]], key=lambda x: x[1]))
