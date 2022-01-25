# var1 = input("Please type in a number: ")
# var2 = input("Please type in another number: ")
# var3 = input("Please type in yet another number: ")
# 
# # comparators
# # == equals
# # != not 
# # < less than
# # > greater than
# # <=
# # >=
# 
# # Boolean Logic AND, OR, NOT.
# 
# if (var1 == var2 or not(var1 != var3)) or var2 == var3:
#     print("My boolean is outputing true")
# else:
#     print("My boolean is outputting false")
# 
# # AND  | in1 | in2 | OUT
# #------+-----+-----+-----
# #      |False|False| FALSE
# #      |False|True | FALSE
# #      |True |False| FALSE
# #      |True |True | TRUE
# 
# treevar1 = input("Type in a tree: ")
# trees = ["Larch","Oak","Pine","Willow"]
# 
# 
# if treevar1 in trees:
#     print("You have typed a tree that was in my list")
# else:
#     print("FAIL")

numvar1 = int(input("Type in a number: "))
if numvar1 < 10:
    print("your number is a single digit integer")
elif numvar1 < 100:
    print("You have a 2 digit integer")
elif numvar1 < 1000:
    print("You have a 3 digit integer")
elif numvar1 < 10000:
    print("You have a 4 digit integer")
else:
    print("That's a big number!")

if numvar1 < 10:
    if numvar1 > 10 and numvar1 < 100:
        print("your number is a two digit number")
    else:
        print("you have a big number")
else:
    print("your number is a single digit integer")
