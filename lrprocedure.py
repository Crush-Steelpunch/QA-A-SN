def lrTestMethod(invar1):
    if invar1 < 5:
        invar1 = invar1 + 5
        return [invar1, True]
    else:
        invar1 = invar1 - 5
        return [invar1, False]


x = 1000
y = 2000
z = x * y
datafromfunc = lrTestMethod(z)
print("test z was ", datafromfunc)
z = y - x
print("test z was ", datafromfunc[1])
z = y * (x/2)
print("test z was ", datafromfunc[1])
z = x * x
print("test z was ", datafromfunc[1])
z = y * y
print("test z was ", datafromfunc[1])
