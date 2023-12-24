def fun(x,y):
    while(x<=y):
        yield x
        x = x+1
for val in fun(1,10):
    print(val)