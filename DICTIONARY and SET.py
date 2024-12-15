marks= {
    "Harry":41,
    "shubh":66,
    "jkjk":56,
    "list":[1,3,5]
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"shubh":100})
print(marks)
marks.update({"deepa":82})
print(marks)
print(marks.get("shubh2"))
print(marks["shubh2"])
d={}#empty dicti
#SET
# f={ 1,2,3,4,7,5,3,1,6,"dep"}
# print(f,type(f))
# f.add("hello")

# print(f)
s1={1,4,5,6}
s2={6,4,7,9}
# print(s1.union(s2))
# print(s1.intersection(s2))
print({1,4}.issubset(s1))
trans={
    "prem":"Love",
    "kursi":"chair",
    "naam":"Name"
    
}
word=input("Enter the word you want meaning of: ")
print(trans[word])
d={}
print(type(d))
d={}
name=input("Enter friends name:")
lang=input("enter the lang: ")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("enter the lang: ")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("enter the lang: ")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("enter the lang: ")
d.update({name:lang})
print(d)
