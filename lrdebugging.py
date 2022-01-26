import pdb
import lrfunctions

pdb.set_trace()

revwrd = input("TYPE: ")
outfuncva = lrfunctions.reverseastring(revwrd)


for i in range(5):
    print("pies")


if 5 > 10:
    print("5 is less than 10")
else:
    print("5 is greater than 10")


industrial_testing={"valve1":True,"valve2":True,"valve3":True,"valve4":False,"valve5":True,"valve6":True,"valve7":True,"valve7":True}
help(industrial_testing)

for i in industrial_testing.keys():
    if not industrial_testing[i]:
      print("Valve is in error, stop everything!")
      break
    # Further testing code would go here?
    print(i,"Is Fine")

for i in "Spoooooooooooon":
    print(i)