import random
'''
1 for snake 
-1 for water 
0 for gun
'''
computer=random.choice([1,0,-1])
youStr=input("Enter the number: ")
youDic={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDic[youStr]
print(f"You choose {reverseDict[you]}\nComputer choose  {reverseDict[computer]}")
if(computer==you):
    print("It's Draw")
elif(computer==-1 and you==1):
    print("You Win!")
elif(computer==-1 and you==0):
    print("You Lose")
elif(computer==0 and you==1):
    print("You Win")
elif(computer==0 and you==-1):
    print("You Lose")
elif(computer==1 and you==0):
    print("You Lose")
elif(computer==1 and you==-1):
    print("You Win")
else:
    print("Something Went Wrong")
