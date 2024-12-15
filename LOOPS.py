for i in range(1,6):
    #      print(i)
 i=0
while(i<6):
    print("Hello")
    i+=1
  
  
l=["hARRY",9,"hii","rohan",56,23]
i=0

while(i<len(l)):
    print(l[i])
    i+=1

for i in range(4):
    print(i)


l=[1,2,3,4,5]
for i in l:
    print(i)

t=(45,76,98,90)
for i in t:
    print(i)
    
s="Naina"
for i in s:
    print(i)


l=[1,6,8,8]
for item in l:
    print(item)
else:print("done")
s=input("Enter the string")
if(s==s[: : -1]):
    print("Palindrome")
else:
    print("Not Palindrome")
    
# to reverse the number
n=5464
rev=0
while(n!=0):
    
    r=n%10
    rev=rev*10+r
    n=n//10 
 #for dividing in python we use//
print(rev)

# for printing the # in sequence
print("#",end=" ")
print("#",end=" ")
print("#",end=" ")
print("#",end=" ")

for i in range(4):
  for j in range(4-i):
    print("#",end=" ")
print()

n=int(input("Enter the number"))
fact=1
if n< 0:
   print("Enter the valid no:")
elif n==0:
    print(fact)
else:
   for i in range(1,n+1):
     fact=fact*i

print(fact)


num_terms=int(input("Enter the number"))
a=0
b=1
c=0
while(c<=num_terms):
    a=b
    b=c
    c=a+b
    print(c)
for i in range(1,100):
  print(i)
  if(i==35):
    break
for i in range(5):
  print(i)
  if(i==3):
    continue
print(i)

n=["Harry","Naina","Sachin","Sahul"]
for name in n:
  if(name.startswith("S")):
    print(f"Hello,{name}")
num = int(input("Enter the number: "))
c=0
for i in range(1,num+1):
  if(num%i==0):
    c=c+1
if(c>2):
  print("Number is prime")
n=int(input("enter the number: "))
for i in range(2,n):
      if(n%i==0):
          print("Number is not prime")
          break
else:
      print("Number is prime")

n=int(input("enter the number: "))
sum=0
i=1
while(i<=n):
      sum+=i
      i+=1
print(sum)
n=int(input("enter the number: ")) 
fact=1
for i in range(1,n+1):
  fact*=i
  i+=1
# print(fact)
n=3
for i in range(1,n+1):
   print(" "* (n-i),end="")
   print("*"* (2*i-1),end="")
   print(" ")
n=7
for i in range(1,n+1):
  if(i==1 or i==n):
     print("*"*n,end="")
  else:
         print("*",end="")
         print(" "*(n-2),end="")
         print("*",end="")
  print("")

n=int(input("Ente the number: "))
for i in range(1,11):
      print(f"{n}x{11-i}={n*(11-i)}")


