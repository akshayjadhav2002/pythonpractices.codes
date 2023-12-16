#Creating the object of class gives the memory for class and its method and vriables
class company:
    def dip(self):  # here self acts as "this" keyword and  takes memory address as parameter
        print("Hello")
print("Start Code")

obj = company() ## --> internally automatically calls the __new__() method which allocates memory
                #---> and after the method __init__() is called which creates constructor and memory

obj.dip()   #internally it pass the object as the parameter to the to dip(object)
print("End code")
