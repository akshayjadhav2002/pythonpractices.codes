#from program2 import*
from abc.py import *
class Core2web(ABC):
    def __init__(self):
        print("In Core2web object")

class Incubators(Core2web):
    def __init__(self):
        print("In Incubators Object")
        super().__init__()

if __name__ =="__main__":
    Incubators()
    #Binecaps()
else:
    Binecaps()

#Recursive importing is not supported and while importing the imported file
#is on head of current file or simply above it.
# when we call the object of class while is below its call or simply the class is not yet declared and we are 
# creating the object of it and call the constructor of it so it will simply give the error of NameError :- Name not found 
    