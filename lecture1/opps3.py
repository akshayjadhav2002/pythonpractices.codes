def fun ():
    print("In fun1")
def fun ():
    print("In fun2")

fun()
fun(10)
### In fun2 [ it is o/p because fun 1 is  overridden by fun2]
###TypeError: fun() takes 0 positional arguments but 1 was given 
