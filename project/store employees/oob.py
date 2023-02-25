class Employee:

    count=0
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
        Employee.count+=1
    def displayCount(self):
        print("Total Employee %d" % Employee.count)  

    def displayDetails(self):
        print("Name : ", self.name,  ", Position: ", self.position, ", Salary: ", self.salary)  

emp1=Employee("John","Manager",5000)
emp2=Employee("David","Clerk",3000)
emp1.displayDetails()    
emp1.displayCount()    