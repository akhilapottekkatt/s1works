class employee():
    company_name="ABCD"
    place="calicut"
    def __init__(s,id,name,salary):
        s.emp_id=id
        s.emp_name=name
        s.emp_salary=salary
    def print_det(self):
        print(self.emp_id,self.emp_name,self.emp_salary)

emp1=employee(11,"hari",4000)
emp2=employee(12,"janu",25000)
emp1.print_det()
emp2.print_det()
