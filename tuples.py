a=(1,2,3)
print(type(a))
b=("stri")
print(type(b))
c=(1,)
print(type(c))
d=("apple","banana","mango","grapes")
print(len(d))

tup1=(10, 20, 30, 40, 50)
print(tup1)
print(tup1[0])
print(tup1[-1])

tup2 = (10, 20, 30, 40, 50, 60)
print(tup2[:3])
print(tup2[-3:])

tup3 = (5, 10, 15, 10, 20, 10, 25)
print(tup3.count(10))

tup4=(10, 20, 30, 40, 50)
print(tup4.index(40))

tup5=(10, 20, 30, 40, 50)
lst=list(tup5)
lst.append(60)
lst.append(70)
print(lst)
tup6=tuple(lst)
print(tup6)

tup7=(10, 20, 30, 40, 50)
tup8=(60,70)
tup9=tup7+tup8
print(tup9)

tup10 = (10, 20, 30, 40, 50, 60)
print(tup10[::-1])

tup11 = (10, 20, 30, 40, 50, 60, 70)
print(tup11[0::2])

tup12 = (10, 20, 30, 40, 50)
a,b,c,d,e=tup12
print(a)

print(c)

print(e)

tup13=(10, 20, 30, 40, 50)
(first,*middle,last)=tup13
print(first)
print(middle)
print(last)

tup14 = (10, 20, 30, 40, 50)
print(tup14[0:3])