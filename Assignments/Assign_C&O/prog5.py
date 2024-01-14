class captain:
    def __init__(self,Name,Country):
        self.Name = Name
        self.Country =Country
    def captainInfo(self):
        print(self.Name)
        print(self.Country)

class player(captain):
    def __init__(self,Name,Country,PlayerName):
        self.Name = Name
        self.Country =Country
        self.PlayerName = PlayerName
        
    def captainInfo(self):
        print(self.Name)
        print(self.Country)
        print(self.PlayerName)
        
obj = player("Rohit","IND","virat")
obj.captainInfo()
captain("Rohit","IND").captainInfo()
