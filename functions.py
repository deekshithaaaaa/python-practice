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

