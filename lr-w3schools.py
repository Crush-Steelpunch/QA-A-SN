asterix = "* "
printvar = ''

for i in (1,2,3,4,5,4,3,2,1):
    for j in range(i):
        printvar = printvar + asterix
    print(printvar)
    printvar = ''
