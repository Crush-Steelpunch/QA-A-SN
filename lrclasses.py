import pdb
class Dog:
    #energy = "High"

    def __init__(self,energy="High",foodtype="dry",barktype="woof"):
        self.energy = energy
        self.foodtype = foodtype
        self.barktype = barktype


    def speak(self):
        print(self.barktype)

pdb.set_trace()
ll

lassie = Dog("superhigh","wet")


clifford = Dog()

Bolt = Dog("Lightening","organic")

lassie.speak()
clifford.speak()
#Bolt.energy = "lightening"
print(lassie.energy)
print(clifford.energy)
print(Bolt.energy)
print("Lassie eats",lassie.foodtype,"food.")
print("Bolt eats",Bolt.foodtype,"food.")