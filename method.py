class Employee:
    increment=1.5
    no_of_employees=0
    def __init__(self,fname,lname,age,salary):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.salary=salary
        Employee.no_of_employees+=1
    def increase(self):
        self.salary=self.salary*self.increment
    @classmethod    
    def change_increment(cls,amount):
        cls.increment=amount
    @classmethod
    def from_str(cls,string):
        fname,lname,age,salary=string.split("-")
        return cls(fname,lname,age,salary)
    @staticmethod
    def isopen(day):
        if day=="Sunday":
            return "Close"
        else:
            return "Open"
class senior_emp(Employee):
    def __init__(self,fname,lname,age,salary,exp,hobby):
        super().__init__(fname,lname,age,salary)
        self.exp=exp
        self.hobby=hobby
    def increase(self):
        self.salary=self.salary*(self.increment(3))
        
sanj=senior_emp("Sanjana","mogaveera",20,40000,8,"Reading story books")
print(sanj.fname)
print(sanj.exp)
prathi=Employee("prathiksha","naik",21,60000)
print(Employee.no_of_employees)
prarthu=Employee("prarathana","naik",15,70000)
prema=Employee.from_str("Prema-naik-43-80000")

print(prathi.salary)
Employee.change_increment(1)
prathi.increase()
print(prathi.salary)

print(prema.fname)
print(prema.age)
print(prema.salary)

print(prathi.isopen("Monday"))
print(prarthu.isopen("Sunday"))
print(Employee.isopen("Tuesday           "))
