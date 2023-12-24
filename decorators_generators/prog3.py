def outerFun():
    print("In outer Function")

    def innerFunction1():
        print("In inner Function1")
    def innerFunction2():
        print("In inner Function2")
    return innerFunction1,innerFunction2
    # innerFunction and innerFunction are the address of inner functions which are returns by the outerFunction
    
ans1,ans2 = outerFun()
ans1()
ans2()
