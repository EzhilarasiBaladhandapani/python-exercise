f = open("D:/read and write/files.txt","r+")
S = []
for line in f:
    value=line.split()
    S.append([value[0]])
print(S)
f.close()

