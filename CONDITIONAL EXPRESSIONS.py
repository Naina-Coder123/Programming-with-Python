
a=int(input("Enter the age:"))
if(a%2==0):
    print("a is even ")
else:
    print("a is odd")

a=input("Enter the number")
b=input("Enter the number")
c=input("Ente the number: ")
d=input("Enter the number:")
if(a>b and a>c and a>d):
    print(a)
elif(b>a and b>c and b>d):
    print(b)
elif(c>a and c>b and c>d):
    print(c)
elif(d>a and d>c and d>b):
    print(d)
marks1=int(input("Enter the number:"))
marks2=int(input("Enter the number:"))
marks3=int(input("Enter the number:"))

total_percentage=((marks1+marks2+marks3)/300)*100
print(total_percentage)
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print('you are pass')
else:
    print("Sorry Try next year")

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("Enter your message:")
if((p1 in message)or (p2 in message) or ( p3 in message) or (p4 in message)):
    print("This comment is a spam")
else :
    print("Not a spam")

username=input("Enter the username")
s=len(username)
if(s<10):
    print("Less than 10 characters , please select another ")
else:
    print("click to next option")

list=["Naina","Deepa","Devanshi"]
to_find=input("Enter the name to find:")
if(to_find in list):
    print("Yes")
else:
    print("No")

marks=int(input("Enter your marks:"))
if(marks<=100 and marks>=90):
    grade="Ex"
elif(marks<=90 and marks>=80):
    grade="A"
elif(marks<=80 and marks>=70):
    grade="B"
elif(marks<=70 and marks>=60):
    grade="C"
elif(marks<=60 and marks>=50):
    grade="D"
elif(marks<=50 ):
    grade="F"
print(grade)

post="NaiNa is travelling india naina is travelling all over the world"
if("Naina".lower()in post.lower()):
    print("This post is talking about naina")
else:
    print(" This post is not talking about harry")
  