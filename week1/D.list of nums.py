A = [1,2,3,3,3,4]

X= []
for B in A:
    if not(B in X):
        X.append(B)
print(X)        