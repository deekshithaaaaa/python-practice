class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    pass
dog=Dog()
dog.eat()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"Name:{self.name}\n Age:{self.age}"
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
stu=Student("Dee",21,1)
print(stu.roll_no)
print(stu.display())

class Vehicle:
    def start(self):
        return "Vehicle is started"
class Car(Vehicle):
    def drive(self):
        return "Car is driving"
c1=Car()
print(c1.drive())
print(c1.start())

class Animal:
    def sound(self):
        return "Animal makes sound"
class Dog(Animal):
    def sound(self):
        print( super().sound())
        print ("Dog barks")
d1=Dog()
print(d1.sound())

class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
class Student(Person):
    def __init__(self,name,age,city,course):
        super().__init__(name,age,city)
        self.course=course
s1=Student("Dee",21,"Hyd","Python")
print(s1.name)
print(s1.age)
print(s1.city)
print(s1.course)

class Person:
    def walk(self):
        return "Person is walking"
class Employee(Person):
    def work(self):
        return "Employee is working"
class Manager(Employee):
    def code(self):
        return "Manager is coding"
m1=Manager()
print(m1.walk())
print(m1.work())
print(m1.code())

class Employee:
    def work(self):
        return "Employee is working"
class Developer(Employee):
    def code(self):
        return "Developer is coding"
class Tester(Employee):
    def test(self):
        return "Tester is testing"
d1 = Developer()
t1 = Tester()
print(d1.work())
print(d1.code())
print(t1.work())
print(t1.test())

        
class Printer:
    def Pmethod(self):
        return "This is printer method"
class Scanner:
    def Smethod(self):
        return "This is scanner method"
class Machine(Printer, Scanner):
    def Mmethod(self):
        return "This is machine method"
obj = Machine()
print(obj.Pmethod())
print(obj.Smethod())
print(obj.Mmethod())



class Person:
    def Pmethod(self):
        return "This is person method"
class Student(Person):
    def Smethod(self):
        return "This is student method"
class Employee(Person):
    def Emethod(self):
        return "This is employee method"
class Intern(Student, Employee):
    def Imethod(self):
        return "This is intern method"
obj = Intern()
print(obj.Pmethod())
print(obj.Smethod())
print(obj.Emethod())
print(obj.Imethod())