input="Hello"
print(input[::-1])

s=int(input("Enter a num:"))
t=str(s)
p=t[::-1]
q=int(p)
if s==q:
    print("Palindrome")
else:
    print("Not a palindrome")

num=12345
rev=0
digit=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

num=int(input())
if num==2:
        print("Prime")
elif  num%1==num and num%num==1 and num%2!=0:
        print("prime")
else:
        print("Not prime")