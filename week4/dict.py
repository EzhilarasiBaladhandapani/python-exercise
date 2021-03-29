f = open("D:/read and write/dict.txt","r")
s = {}
for line in f:
    (key, value) = line.split()
    s[int(key)]= value
print(s)
f.close()    
    