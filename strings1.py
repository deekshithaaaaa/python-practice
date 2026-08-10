str1="Hello World"
print(len(str1))

str2="python programming"
print(str2.upper())
print(str2.lower())

str3=" openai "
print(str3.rstrip())
print(str3.lstrip())
print(str3.strip())

str4="Artificial Intelligence"
print(str4[:5])

str5="Python" 
print(str5[::-1])

str6="banana"
print(str6.count("a"))

str7="machine learning"
print(str7.replace(" ","-"))

str8="red,green,blue" 
print(str8.split())

str9="Python is Fun"
a=str9.split()
print(a[2])

str10="datascience"
print(str10.startswith("data"))
print(str10.endswith("science")) 

str11="madam"
org="madam" 
rev=str11[::-1]
if rev==org:
    print("palindrome")
else:
    print("not")

str12="hello world"
print(str12.title())

str13="12345"
print(str13[::2])

str14="I love Python programming"
print(str14.replace("Python","Java"))

str15="This is a book. It is useful."
print(str15.count("is"))