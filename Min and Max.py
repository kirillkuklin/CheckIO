def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        args = args[0]
    big = None
    for d in args:
        if big == None or key(d) > key(big):
            big = d
    return big

def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        args = args[0]
    low = None
    for d in args:
        if low == None or key(d) < key(low):
            low = d
    return low
