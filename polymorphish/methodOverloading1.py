def add(x = 10,y=None,z=None):
    return x+y+z

#print(add(10)) #TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
print(add(10,20,30)) 
#print(add(10,20)) TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'