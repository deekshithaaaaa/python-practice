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
