def gun():
    print("In gun")
def run(y):
    print("In run")
    y()
def fun(x):
    print("In fun")
    
fun(run(gun))
