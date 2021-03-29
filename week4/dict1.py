
f = open("D:/read and write/dict1.txt","r+")
#f = ["haii","ezhil","hwr","aaa"]
for i in f:
    a = i.strip("  ,v ?")
    print(a)
    y=a.split(",")
    print(y)
x=enumerate(y)
z=(list(x))
print(*z)
x1=str(z).replace('(','')
x2=x1.replace(')','')
print(x2)



