class parent():
    def property(self):
        print("Gold,Silver,Etc")
    def career(self):
        print("Engg")

class child(parent):
    def career(self):
        print("youtuber")

obj1 =child()


obj1.property()
obj1.career()

parent().property()
parent().career()

#Gold,Silver,Etc
#youtuber