import pdb
pdb.set_trace()

openedfile = open("README.md")
textstuff = openedfile.readlines()
openedfile.close()
print(textstuff)
#uppertext = textstuff.upper()
textstuff.insert(4,"Here is a line I inserted\n")
print(textstuff)
#print(uppertext)
openedfile = open("README.md","w")
openedfile.writelines(textstuff)
openedfile.close()