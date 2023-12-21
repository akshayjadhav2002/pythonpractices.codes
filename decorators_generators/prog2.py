def outerFun():
    print("In outer Function")
    def innerFunction1():
        print("IN inner Function-1")
    def innerFunction2():
        print("In inner Function-2")
    innerFunction1()
    innerFunction2()
outerFun()