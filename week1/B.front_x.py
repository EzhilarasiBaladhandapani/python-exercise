A = ["xxx","zzz","vzv","zzb","nzn"]
Xlist = []
Ylist = []
for B in A:
    if B.startswith('z'):
        Xlist.append(B)
    else:
        Ylist.append(B)
print(sorted(Xlist) + sorted(Ylist))        