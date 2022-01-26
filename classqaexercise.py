#In a new Python file,  DONE
#create a class of students. DONE

#It should contain the following attributes: 
# - name,   DONE
# - age, and  DONE
# - class   DONE (as classname)
# with default value "student".  DONE

#It should also contain a method  DONE
# which takes in 3 test scores and  DONE
# calculates the students average test score. DONE
# prints the resulting score  DONE (as return for main program to print)

class Students:

    def __init__(self, age, classname,name="student"):
        self.age = age
        self.classname = classname
        self.name = name

    def calcavgscore(self,score1:int ,score2:int ,score3:int):
        avgscore = (score1 + score2 + score3)/3
        return avgscore

Cecilia = Students(31, "spoon art",[5,5,5])
Rafael = Students(27, "flower arranging")
Brooklynn = Students(45, "Ballistic Weapons")

print( "Cecilia: ", Cecilia.calcavgscore(5, 5, 5))
print( "Rafael: ", Rafael.calcavgscore(10, 5, 7))
print( "Brooklynn: ", Brooklynn.calcavgscore(20, 10, 0))
