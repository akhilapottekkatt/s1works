class car_details:
    company=0
    prize=0
    clr=0
    def car(self):
        print("car deatils company of car:",self.company,"prize of car:",self.prize,"color of car is:",self.clr)
car1 =car_details()
car1.company="zuzuki"
car1.prize=300000
car1.clr="blue"
car1.car()


        
car2=car_details()
car2.company="shift"
car2.prize=400000
car2.clr="red"
car2.car()

car3=car_details()
car3.company="toyotta"
car3.prize=500000
car3.clr="green"
car3.car()
