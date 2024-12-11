class employ_details():
    basic=0
    TA=0
    DA=0
    def salary(self):
        print("total salary of employ 1:",self.basic+self.TA+self.DA)
emp1=employ_details()
emp1.basic=20000
emp1.TA=5000
emp1.DA=2000
emp1.salary()
