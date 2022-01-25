listvar1 = ("meat","veg","cake","beer for the weekend",20)
#              0     1      2        3
#             -4    -3     -2       -1
# [] square brackets
# () parenthesise
# {} curly brackets
# <> angle brackets / greek brackets
# < bra   > ket




print(len(listvar1))
print(listvar1.count("veg"))
#print(listvar1
print(listvar1[2][2])


var1 = "I am Leon and I am typing a line"
print(var1[1])
print(var1.count("a"))


cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

#print(cool_animals[1][1])

# Dictionaries

dictvar1 = { "cow":"moo" ,"sheep":"baa"   , "chicken":"cluck"  , "dog":"bowwow" }
print(dictvar1["dog"])
print(dictvar1.items())
print(dictvar1.keys())
print(dictvar1.values())

dictvar1["lemming"] = "squeek"

print(dictvar1)