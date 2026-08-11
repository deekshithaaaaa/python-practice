for i in range(1,11):
    print(i)
    i=i+1

for i in range(2,21,2):
    print(i)

total=0
for i in range(1,11):
    total=total+i
print(total)

num=5
for i in range(1,11):
    print(num,"*",i,"=",num*i)

total=0
for i in range(1,51):
    if i%2==0:
       total=total+i
print(total)

total=0
for i in range(1,31):
    if i%2!=0:
        print(i)
        total=total+i
print(total)

for i in range(10,0,-1):
    print(i)

fact=1
for i in range(5,0,-1):
    fact=fact*i
print(fact)

numbers = [12, 45, 7, 89, 23, 56]
largest_num=0
for i in range(len(numbers)):
    if numbers[i]>largest_num:
        largest_num=numbers[i]
        i+i+1
print(largest_num)
i=1
while i<=10:
    print(i)
    i=i+1

i=10
while i>=1:
    print(i)
    i=i-1

i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1
print(sum)

i=2
while i<=20:
    print(i)
    i=i+2

i=1
while i<=30:
    if i%3==0:
        print(i)
    i=i+1

i=1
count=0
while i<=50:
    if i%5==0:
        count=count+1
    i=i+1
print(count)





