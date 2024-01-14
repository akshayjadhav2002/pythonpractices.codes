class A:
    pass
class c(A):
    pass
class B(c):
    pass

class D(c):
    pass

class E(D,B):
    pass


print(E.__mro__)