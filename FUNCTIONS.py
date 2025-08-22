# # def print():
# #     print("HELLO")
  
# # print(print())


# def avg():
#   a=int(input("Enter the number"))
#   b=int(input("Enter the number"))
#   c=int(input("Enter the number"))
#   averag=(a+b+c)/2
#   print(averag)  

# avg()

# def goodday(name,ending):
#   print("Good Day,  "+ name)
#   print(ending)
#   return "done "
# a=goodday("Naina","thankyou")
# print(a)
 
 
# def goodday(name,ending="thankyou"):
#       print(f"Good Morning,{name}")
#       print(ending)
# goodday("Naina","Thanks")


# # Practice set 
# def fun(a,b,c):
#       if(a>b and a>c):
#             return a
#       elif(b>a and b>c):
#             return b
#       else:
#             return c

# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# c=int(input("enter the number: "))
# p=fun(a,b,c)
# print(p)

# def temp(f):
     
#       c=5*(f-32)/9
#       print(c)
# f=int(input("Enter the number:"))
# temp(f)


# print("a")
# print("b")
# print("c",end=" ")
# print("d",end=" ")


# # sum of a number by recursively
# def sum(n):
#       if(n==1):
#             return 1
      
#       return sum(n-1)+n

# n=int(input("Enter the number: "))
# print(sum(n))


# def pattern(n):
#     if(n==0):
#           return
#     print("*"*n)
#     pattern(n-1)
# n=int(input("Enter the number: "))
# pattern(n)

# def inch_to_cms(inch):
#   return inch*2.54
# n=int(input("Enter the number: "))
# print(f"the corresponding value in cms is({inch_to_cms(n)})")

# def rem(l,word):
#       n=[]
#       for item in l:
#             l.remove(word)
#             return l
# l=["Harry","Rohan","soham","an"]
# print(rem(l,"an"))
# def f1():
#       print("Hello World")
# print(f1())
# print(type(f1))

# x1={0:1,False:'a','b':True,1:{2,3,5,1}}
# # x2={{1,2}:{1,2}}
# y={1,2,3,4,5}
# print(x1)
# # print(type({}))
# for i in x1.items():
#       print(i)

def f2(l1):
      return "Hello"
print(f2())
      