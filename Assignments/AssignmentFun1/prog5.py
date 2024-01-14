def outer():
    def inner(outer):
        print(outer)
        return inner
    return inner(outer)

if __name__ == "__main__":
    retObj = outer()
    print(retObj)

##<function outer at 0x0000028D487C8A40>
##<function outer.<locals>.inner at 0x0000028D489ECEA0>