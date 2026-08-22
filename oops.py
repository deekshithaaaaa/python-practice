class Student():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def open(self):
        return "Student opening book"
    def write(self):
        print (f"Student name is {self.name}")
obj1=Student("Dee",101,97)
obj2=Student("Alex",102,85)
obj3=Student("Emily",103,67)
print(obj1.name,obj1.roll_no,obj1.marks)
print(obj2.name,obj2.roll_no,obj2.marks)
print(obj3.name,obj3.roll_no,obj3.marks)
print(obj1.open())
obj1.write()
print(obj2.open())
obj1.write()
print(obj3.open())
obj1.write()

class Dog:
    def __init__(self,color,breed,height):
        self.color=color
        self.breed=breed
        self.height=height
    def bark(self):
        return f"{self.breed} is barking"
    def eat(self):
        print(f"{self.breed} is eating")
dog1=Dog("Black","German Shepherd","55cm")
dog2=Dog("Gold","Golden Retriever","51cm")
dog3=Dog("Black","Labrador Retriever","54cm")
print(dog1.breed,dog1.color,dog1.height)
print(dog1.bark())
dog1.eat()
print(dog2.breed,dog2.color,dog2.height)
print(dog2.bark())
dog2.eat()
print(dog3.breed,dog3.color,dog3.height)
print(dog3.bark())
dog3.eat()

class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display_details(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Salary:",self.salary)
emp1=Employee("Dee",101,50000)
emp2=Employee("Vini",102,35000)
emp1.display_details()
emp2.display_details()

class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
acc1=BankAccount("Skylar",10090,64579)
acc2=BankAccount("Richard",10274,74892)
print(acc1.deposit(5000))
print(acc2.deposit(6000))

class Car:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed
    def accelerate(self,amount):
        self.speed+=amount
        print(self.speed)
car1 = Car("Toyota", "Camry", 80)
car2 = Car("BMW", "X5", 100)
car1.accelerate(20)
car2.accelerate(30)
    
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def discount(self,percent):
        self.price=self.price-((percent/100)*self.price)
        return self.price
book1 = Book("Atomic Habits", "James Clear", 500)
book2 = Book("The Alchemist", "Paulo Coelho", 400)
print(book1.discount(10))
print(book2.discount(50))