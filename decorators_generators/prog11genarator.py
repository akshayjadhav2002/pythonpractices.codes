def fun():
    print("start fun")
    yield 10
    yield 20
    yield 30
    print("End fun")

#for i in fun():
    #print(i)
fun()