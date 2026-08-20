x = lambda a : a + 10
print(x(5))

y=lambda b:b*b
print(y(6))

x=lambda n:n%2==0
print(x(5))

y=lambda b:b*b*b
print(y(6))

a=lambda x:x==x[::-1]
print(a("dad"))

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(result)

words = ["apple", "banana", "mango"]
result = list(map(lambda x: x.upper(), words))
print(result)

words = ["apple", "cat", "banana"]
result = list(map(lambda x: len(x), words))
print(result)


numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

numbers = [20, 55, 70, 40, 90]
result = list(filter(lambda x: x > 50, numbers))
print(result)

names = ["Arun", "Priya", "Anu", "Ravi", "Akash"]
result = list(filter(lambda x: x.startswith("A"), names))
print(result)

words = ["cat", "apple", "dog", "banana", "sun"]
result = list(filter(lambda x: len(x) > 3, words))
print(result)

numbers = range(1, 21)
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)


from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)

numbers = [10, 45, 23, 78, 12]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)

words = ["Hello", " ", "World"]
result = reduce(lambda x, y: x + y, words)
print(result)


fruits = ["Apple", "Banana", "Mango"]
for index, item in enumerate(fruits):
    print(index, item)

shopping = ["Milk", "Bread", "Eggs", "Fruits"]
for index, item in enumerate(shopping, start=1):
    print(index, item)