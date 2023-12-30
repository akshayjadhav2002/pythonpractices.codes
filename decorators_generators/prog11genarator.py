def fun():
    print("start fun")
    yield 10           # takes the 10 and go back to the fun call by maintaining Prog COunter
    yield 20
    yield 30
    print("End fun") #after yield it is not prefered to write the print line 

for i in fun():
    print(i)
