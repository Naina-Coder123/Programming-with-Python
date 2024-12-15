def print():
    print("HELLO")
  
print()


def avg():
  a=int(input("Enter the number"))
  b=int(input("Enter the number"))
  c=int(input("Enter the number"))
  averag=(a+b+c)/2
  print(averag)  

avg()

def goodday(name,ending):
  print("Good Day,  "+ name)
  print(ending)
  return "done "
a=goodday("Naina","thankyou")
print(a)
 
 
def goodday(name,ending="thankyou"):
      print(f"Good Morning,{name}")
      print(ending)
goodday("Naina","Thanks")

