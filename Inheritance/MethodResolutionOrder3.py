class Boss:
    def report(self):
        print("I am the boss")
    
class Manager1(Boss):
    def report(self):
        print("Manger1:report to Boss")
    
class Manager2(Boss):
    def report(self):
        print("Manger2:report to Boss")
class TeamLead1(Manager2,Manager1):
    def report(self):
        print("TeamLead:report to manger 1 and 2")
class TeamLead2(Manager2,Manager1):
    def report(self):
        print("TeamLead:report to manager 2")

class Devloper(TeamLead1,TeamLead2):
    pass

print(Devloper.__mro__)


" " " (<class '__main__.Devloper'>, <class '__main__.TeamLead1'>, <class '__main__.TeamLead2'>, " " "
" " "<class '__main__.Manager2'>, <class '__main__.Manager1'>, <class '__main__.Boss'>, <class 'object'>) " " "

## The teamlead 2 should have the same order of sequencce as the teamlead 1 ..