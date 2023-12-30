class parent(object):
    def __init__(self):
        print("In constructor-1")
    
    def __init__(self): #constructor 2 is overrriden
        print("In constructor -2")

obj = parent()
