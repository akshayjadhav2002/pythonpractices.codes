def outerFun():
    print("In outer Function")

    def innerFunction1():
        print("In inner Function1")
    def innerFunction2():
        print("In inner Function2")
    return innerFunction1,innerFunction2
ans1,ans2 = outerFun()
ans1()
ans2()
