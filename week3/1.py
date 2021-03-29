
import re
f = open("D:/REG EXP/data.txt","r")
d =open("D:/REG EXP/data1.txt","w")
y = re.findall('[\w.-]+@gmail.com',f.read())
print (y)
z=(y[-5:])
print (z)
count1=len(y)
if count1>4:
    d.write(str(z))   
else:
    print(y)

f.close()
d.close()               