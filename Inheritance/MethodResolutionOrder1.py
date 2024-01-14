class Boss:
    def report(self):
        print("i am the boss")
        
class Manager(Boss):
    def report(self):
        print("Manager:Report to Boss")

class TeamLead(Boss,Manager):
    def report(self):
        print("TeamLead:Report to Manager and Boss")

class Devloper(TeamLead):
    def report(self):
        print("Dev:Report to TeamLead")

print(Devloper.__mro__)  
print(Devloper.mro())  



##TypeError: Cannot create a consistent method resolution
##order (MRO) for bases Boss, Manager

## MRO Rule :-If any class has two parents and if then have parent child relattionship
## then in th order chid should be first and then child.   