class Employee:
    def __init__(self,name,salary):
        #public attribute
        self.name=name
        #private attribute
        self.__salary=salary
    def show(self):
        print(self.name,self.__salary)

emp=Employee("akhi",4000)
emp.show()
print(emp.name)
#print(emp.salary)  this didint print because its an private attribute this only print
#inside of the class thats y its print when call show function
