def sq(x, y):
    return x ** y

def tri(z):
    z = int(z)
    z = z ** 3
    return z

print(tri(sq(12, 2)))
print(tri(12))
print(tri(24))