class Person:
    def __init__(self,fname,lname,city):
        self.fname=fname
        self.lname=lname
        self.city=city

    def printPerson(self):
        print("Person ",self.fname,self.lname,self.city)


class Emp(Person):
    def __init__(self,fname,lname,city,doj,department):
        super().__init__(fname,lname,city)
        self.doj=doj
        self.department=department


    def sayHello(self):
        print("Hello ",self.fname," Welcome to department ",self.department)

    def printPerson(self):
        print("Emp ",self.fname)


emp1=Emp("Steve","John","LA","01-01-2020","devOps")     
emp1.sayHello()
emp1.printPerson()   