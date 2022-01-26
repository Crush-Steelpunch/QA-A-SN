def lrTestMethod(invar1):
    if invar1 < 5:
        invar1 = invar1 + 5
        return [invar1, True]
    else:
        invar1 = invar1 - 5
        return [invar1, False]

x = 100
y = 2
z = int(input("NUMIN: "))
print(lrTestMethod(x+2+z+y))