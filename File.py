'''
a="a very long string with emails

emails=[]
3 seconds
'''
# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()

# st="Hey ,How are you?"

# f=open("file.txt","w")
# f.write(st)
# f.close()

# f=open("file.txt")
# line1=f.readlines()
# print(line1,type(line1))
# line2=f.readlines()
# print(line2,type(line2))
# line3=f.readlines()
# print(line3,type(line3))
# line4=f.readlines()
# print(line4,type(line4))
# f.close()
f=open('file.txt')
line=f.readline()
while(line!=" "):
    print(line)
    line=f.readline()
f.close()

