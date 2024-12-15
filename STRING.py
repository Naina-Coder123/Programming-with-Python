name="Harry"
print(name)
nameshort=name[3]
sl=print(name[0:5])
print(nameshort)
print(len(name))
print(name[-4:-1])
print(name[:4])
print(name[1:])
word="Welcome"
print(word[1:5:3])
a="jdckdfkdsfssckdkdjksljskl"
print(a[1:11:4])
print(word.endswith("come"))
print(word.startswith("WE"))

word="welcome wow"
print(word.capitalize())
print(word.count("w"))
print(word.find("wow"))
print(word.replace("wow","Naina"))
a="I want to\\ build a \"kitchen\" user interface\n device "
print(a)
v=int(input("Enter the Name: "))
date=int(input("Enter the date: "))
print(f" Dear { v }, \n You are selected ! \n {date}")
print(f"Good Afternoon ,{ v }")
d=int(input("Enter the date: "))
letter =''' Dear <|NAME|>,
You are selected!
<|date|>'''
print(letter.replace("<|NAME|>","Naina")).replace("<|date|>","5 February 2025")
name="Naina is working   on the  project"
print(name.replace("  "," "))
print(name)
sen="Dear Harry ,\nThis python course is nice. \nThanks"
print(sen)