friend=["Apple",5,"Gun",7.9890,False,"Naina"]
print(friend[0])

friend[0]="Orange"
print(friend)
print(friend[1:3])
l1=[5,7,3,9,0,1]
# l1.insert(2,8347)
# l1.sort()
# l1.reverse()
l1.remove(3)
print(l1)
#TUPLE
a=(1,6,53,6,5)
print(type(a))
b=(3,"Naina",7,False)
b[0]=5
print(b)
print(a)
name=a.count(6)
print(name)
i=a.index(6)
print(i)
repeat=a*3
print(repeat)
print(1 in a)
print(max(a))
slice=a[1:3]
print(slice)
fruits=[]
f1=int(input("Enter the first fruit:"))
fruits.append(f1)
f2=int(input("Enter the second fruit:"))
fruits.append(f2)

f3=int(input("Enter the third fruit:"))
fruits.append(f3)

f4=int(input("Enter the fourth fruit:"))
fruits.append(f4)

f5=int(input("Enter the fifth fruit:"))
fruits.append(f5)
print(fruits)

fruits=[]
f1=int(input("Enter the fruits"))
fruits.append(f1)
m2=int(input("Enter the fruits"))
fruits.append(m2)
m3=int(input("Enter the fruits"))
fruits.append(m3)
m4=int(input("Enter the fruits"))
fruits.append(m4)
m5=int(input("Enter the fruits"))
fruits.append(m5)
m6=int(input("Enter the fruits"))
fruits.append(m6)
m7=int(input("Enter the fruits"))
fruits.append(m7)
fruits.sort()
print(fruits)

l2=[56,78,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,65]
n=l2.count(12)

print(n)