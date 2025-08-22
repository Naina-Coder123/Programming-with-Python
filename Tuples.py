#dictionary
# s={}
# print(type(s))

#set
# s={4,'abc',78.5,(7,8,9)}
# print(s)

#unhashable list
# # s={5,7,[7,2]}
# # print(s)
# t={5,7,True,'abc',1}
# print(t)

#Empty set
# a=set()
# print(type(a))
# a={1,'a',4.5,9}


#using frozen set function
# # b=frozenset(a)
# print(b)

#using add function
# b.add(7)
# print(b)

#to traverse the set 
a={1,2,3,4}
for x in a:
    print(x)
    
p={1,'abc',4,6.5}
p.add(2)
print(p)

p.update([7,9,8])
print(p)

p.remove('abc')
print(p)

# p.remove(10) throws a key error
p.discard(10)#it does not throws a key error
print(p)

#remove the first element of a set
p.pop()
print(p)

#clear the all elements of a set
p.clear()
print(p)

#using union
a={1,2,3,80}
b={10,20,80}
print(a|b)

# using intersectio update
a &= b
print(a)


#using subset and superset
a={2,4,5,6,3,7,8}
b={5,7,4,3,2,7}
print(a<=b)
print(a>=b)

#using copy 
c=a.copy()
print(c)



#using all and any function
y={5,6,4,3,0}
print(all(y))
print(any(y))


#starting with tuple

tup1=(2,3,4,5,6)
print(tup1[0])

#starting  with dictionary
#In Python , a dictionary is mapping betwwn an set of indices (keys) and a set of values 
#The items in a dictionary are key value  pairs 
#in dictionary ,key is immutable and value is mutable
d=dict()
print(type(d))
d={}
print(type(d))
d['JAMES']=45
print(d)
d.update({'Shyam':43})
print(d)
print(d['JAMES'])
d.setdefault('HARI',56)
print(d)
d.update({'JAMES':89})
print(d)
#if key is present then d.update will update the value otherwise add to  the dictionary
#but in d.setdefault it will add the new key but not the update the value if the value is present it will return the same dictionary
d.setdefault('Shyam',23)
print(d)
print(d.get('JAMES'))
print(d.setdefault('JAMES'))
print(d.get('ALICE'))
print(d.setdefault('ALICE'))
print(d.get('SONA','KEY NOT FOUND IN THE DICTIONARY'))
#here the phrase 'key not found in the dictionary'has overridden the none
print(d.setdefault('sona',58))
#here by using the setdefault if the key not found in the dictionary it has added the new key value pair in dictionary
y=d.values()
print(y)
print(type(y))
i=d.keys()
print(i)
print(type(i))
o=d.items()
print(o)
print(type(o))


# for in d.keys():
#     print(i,d[i])
# for k,v in d.items():
#     print(k,v)

l=sorted(d)
print(l)
u=sorted(d.keys())
print(u)
# h=sorted(d.values())
# print(h)
v=sorted(d.items())
print(v)

s=[1,0,1,0,1,0,0,1]
s.sort()
print(s)

p=[2,5,3,7,8,1,9]
g=[]
g.append(p[-1])

for i in range(1, 7):
    if(p[i-1]<p[i]):
        g.append(p[i-1])
print(g)
