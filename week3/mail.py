
import re
f = open("D:/REG EXP/data.txt","r+")
d =open("D:/REG EXP/data1.txt","w")
#print("print the word to be find:")
#x=input()
#print(x)
x1 = " "
y = re.findall('[\w.-]+@gmail.com',f.read())
print (y)

if y:
    x2=x1.join(y)
    count1=len(x2)
    
    count2=count1/2
    print(count2)
    z=(y[-3:])
    print (str(z))
    if count2>3:
        d.write(str(z))
        
    else:
        print(x2)
else:
    print("no") 
f.close()
d.close()               