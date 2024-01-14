x = 10
y =20
# the above to are integers so the belong to integer calss 
# and they both have __add__ method in their call
# but we overloaded the  equal to equal method below this is called as operator overloding

print(x == y) # this internally call the def ___eq__(self,obj) method
print(x.__eq__(y)) # same as above
print(dir(int))