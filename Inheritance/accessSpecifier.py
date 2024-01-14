class demo:

  def __init__(self):
    self.x = 10    #public 

    self._y =20     #protected

    self.__z = 30   #private --> class scope is the scope of private
  
  def __fun(self):
    print("In  fun function")

print(dir(demo))

obj = demo()

print(dir(obj))

print(obj.x)
print(obj._y)
print(obj._demo__z)  ### private variable are not private it useses name mangling 
                     ### and can be accessed outside class
                     # but due to abstraction we cant access it like this

obj._demo__z
obj._demo__fun()

obj1 = demo()
#print(obj==obj1) #True

obj.__eq__(obj1)
# all operators in python are the methods