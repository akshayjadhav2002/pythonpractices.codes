def outer():
    def inner():
        return "This is Innner Function"
    return inner
if __name__ == "__main__":
    retobj = outer()
    retInner = retobj() 
    print(retInner)
    