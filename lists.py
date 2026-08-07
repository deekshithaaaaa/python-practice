#list functions
list_1=[1,2,3,3,4,1,5,9,23]
list_2=["Apple","Kiwi","Banana"]
print(len(list_1))
print(min(list_1))
print(max(list_1))
print(sum(list_1))
print(sorted(list_1))
print(len(list_2))
print(min(list_2))
print(max(list_2))

print(sorted(list_2))

print(ord("A"))

#list methods
list_3=[10,3,4,2,3,22,3,66]
list_3.append(90)
print(list_3)
list_3.append([23,45])
print(list_3)
list_4=["mango","guava"]
list_4.append(list_3)
print(list_4)
print(list_3)
list_3.pop(3)
print(list_3)
print(list_3)
list_3.remove(22)
print(list_3)
print(list_4)
list_4[2][7].remove(23)
print(list_4)
list_5=[32,24,56]
list_5.sort(reverse=False)
print(list_5)
print(sorted(list_5))
list_5.insert(2,45)
print(list_5)
print(list_3.count(3))
print(list_3.index(3))
