#1] TypeError
#print("startCode")
#def add(a,b):
#   print(a)
#   print(b)
#add(10,20)
#add(10)
#print("endCode") 
## TypeError: add() missing 1 required positional argument: 'b' '''

''' def add(a,b):
    print(a+b)

print("Start")
add(10,20)
add(10,"akshay") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("End Code") '''

#2] AttributeError
'''class demo():
    def add(self):
        print("Infun")

obj = demo()
obj.add()
obj.gun() #AttributeError: 'demo' object has no attribute 'gun '''

'''class demo:
    def fun(self):
        print(" In Demo")
    def gun(self):
        print("In gun")
obj = demo()
obj.fun()
obj = None #NoneType Class cha object 
obj.gun() #gun() method he NoneType class made nahi so it will give AttributeError
#AttributeError: 'NoneType' object has no attribute 'gun' '''


#3] NameError

'''class demo:
    def fun(self):
        print("In Fun")
obj =demo()
fun() 
#NameError: name 'fun' is not defined '''

#4] IndexError

'''List1 = [10,"kanha",20,"Ashish"]
print(List1[4]) #IndexError: list index out of range'''

#5] KeyError

'''player ={18:"virat",45:"rohit",7:"Msd"}
print(player[1])
#KeyError: 1 '''
from ExcepTypes1 import memo

'''print("Start code")
obj1 = demo()
obj1.fun()
obj1.gun()
output :-Start code
In Fun
In gun
'''
'''print("start Code")
obj1 = demo()
obj1.fun()
obj1.gun()
NameError: name 'demo' is not defined. Did you mean: 'memo' 
'''

#6] Import Error

'''from ExcepTypes1 import remo,memo,demo
print("Strart code")
obj1 = demo()
obj1.fun()
obj1.gun()
outPut :-ImportError: cannot import name 'remo' from 'ExcepTypes1' '''

#7]valueError

'''def add(x,y):
    return x+y

num1 =int(input("Enter the value 1"))
num2 = int(input("Enter the value 2"))
retval = add(num1,num2)
print(retval)
output:- ValueError: invalid literal for int() with base 10: 'akshay' '''

#8]ZeroDivision Error

'''def add(x,y):
    return x/y
x =122
y=0
add(x,y)
output :- ZeroDivisionError: division by zero '''
