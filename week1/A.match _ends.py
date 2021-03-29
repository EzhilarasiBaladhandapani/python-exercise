A = ["sad","mom","dad"]
count = 0
for B in A:
    print(B)
    if len(B)>=2 and B[0]== B[-1]:
        count += 1
print(count)   