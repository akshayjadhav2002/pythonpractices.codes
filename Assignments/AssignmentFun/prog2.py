def outer():
    def inner():
        return " hello, Im the inner Function!"
    return inner
retObj = outer()
retInner = retObj()
print(retInner)
print(retObj)
