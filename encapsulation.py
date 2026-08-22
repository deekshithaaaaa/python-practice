class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.__marks=marks
    def update_marks(self,increase):
        self.__marks+=increase
    def give_marks(self):
        return self.__marks
stu1=Student("Dee",101,65)
stu2=Student("Lucy",102,78)
stu1.update_marks(7)
print(stu1.give_marks())
stu2.update_marks(-10)
print(stu2.give_marks())


class Person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.__age=age
    def set_age(self,num):
        self.__age+=num
    def get_age(self):
        return self.__age
p1=Person("Erin","F",18)
p2=Person("Issac","M",34)
p1.set_age(4)
print(p1.get_age())

class BankAccount:
   def __init__(self, account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.__balance=balance
   def deposit(self,amount):
       self.__balance+=amount
   def get_balance(self):
       return self.__balance
acc1 = BankAccount("Dee", 101, 5000)
acc2 = BankAccount("Vini", 102, 8000)
acc1.deposit(4000)
print(acc1.get_balance())
acc2.deposit(5000)
print(acc2.get_balance())