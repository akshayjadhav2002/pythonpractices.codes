class vehicle:
    def __init__(self,brand,model,year,speed):
        self.brand =brand
        self.model =model
        self.year = year
        self.speed = speed

    def accelarate(self):
        print("vehicle :-Accelarate with the speed of" ,self.speed)

    def brake(self):
        print("Stopes the vehicle on brake")
    
    def honk(self):
        print("please honk vehicle before overtake")

class car(vehicle):
    def accelarate(self):
        print(" car :-Accelarate with the speed of" ,self.speed)
    def honk(self):
        print("please honk the car vehicle before overtake")


objvehilce = vehicle("Tata","Neo",2023,100)
objCar = car("M&m","XUv700",2023,110)
objCar.honk()
#please honk the car vehicle before overtake