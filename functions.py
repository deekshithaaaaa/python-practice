def greet(name):
    print("Hello", name)

greet("Deekshitha")

def add(a,b):
    return a+b
print(add(3,4))

def check_even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

print(check_even(5))

l=[1,2,3,4,5]
p=map(lambda x:x**2,l)
print(list(p))

l=[1,2,3,4,5]
p=filter(lambda x:x%2==0,l)
print(list(p))

def func1():
    print("Hello, Python Functions!")
func1()

name=input("Enter your name")
def func2():
    return f"Hello {name}!"
print(func2())

def func3(a,b):
    return a+b
print(func3(4,7))

def func4(a):
    return a*a
print(func4(5))

def func5(n):
    if n>0:
        return "positive"
    elif n==0:
        return "Zero"
    else:
        return "negative"
print(func5(-9))

def fun6(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(fun6(3))

def func7(a,b):
    if a>b:
        return f"{a} is larger "
    else:
        return f"{b} is larger"
print(func7(9,12))
    


def func8(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(func8(5))

def func9(l):  
    sum=0
    for i in l:
        sum =sum+i
    return sum
print(func9([1,3,2,4]))

def fun10(l):
    for i in l:
        return max(l),min(l)
print(fun10([1,45,2,34,90]))

def fun11(l):
    even_count=0
    odd_count=0
    for i in l:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count
print(fun11([1,2,3,4,5,6,7,8]))

def func12(l):
    sum=0
    for i in l:
        sum=sum+i
    avg=sum/len(l)
    return avg
print(func12([1,2,3,4,5,5]))