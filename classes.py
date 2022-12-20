class Person:
    name=''
    skills=[]
    def __init__(self,name):
        self.name=name
    def addSkills(self, skill):
        self.skills.append(skill)
p1=Person('ashok')
p1.addSkills('Python developer!')
print(p1.name)

class p1(Person):pass
class p2(p1,Person):
    pass
print(p2.__mro__)

def numVal(int):
    print('from int')
def numVal(float):
    print('from float')
numVal(2)