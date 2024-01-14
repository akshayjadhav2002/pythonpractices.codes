class Boss:
    def report(self):
        print("I am the boss")
    
class Manager1(Boss):
    def report(self):
        print("Manger1:report to Boss")
    
class Manager2(Boss):
    def report(self):
        print("Manger2:report to Boss")
class Manager3(Boss):
    def report(self):
        print("Manger3:report to Boss")

class TeamLead1(Manager2,Manager1):
    def report(self):
        print("TeamLead:report to manger 1 and 2")
class TeamLead2(Manager2,Manager3):
    def report(self):
        print("TeamLead:report to manager 2")

class Devloper(TeamLead2,TeamLead1):
    pass

print(Devloper.__mro__)

" " " (<class '__main__.Devloper'>, <class '__main__.TeamLead2'>, <class '__main__.TeamLead1'>, <class '__main__.Manager2'>, " " "
" " "<class '__main__.Manager3'>, <class '__main__.Manager1'>, <class '__main__.Boss'>, <class 'object'>) " " "

# It teace back and starts the search from the back teamlead2 so now it gores to the  manager 3 and then manager1