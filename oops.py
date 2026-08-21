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