from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Dog is Barking"
d1=Dog()
print(d1.sound())

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self,r):
        return 3.14*r*r
class Rectangle(Shape):
    def area(self,l,b):
        return l*b
c1=Circle()
r1=Rectangle()
print(c1.area(3))
print(r1.area(3,4))
        