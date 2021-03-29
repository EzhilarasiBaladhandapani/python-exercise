A = [9,6,3]
B = [10,4,8,6]
result =[]
while len(A) and len(B):
    if A[0]<B[0]:
        result.append(A.pop(0))
    else:
        result.append(B.pop(0))   
result.extend(A)
result.extend(B)
print(result)         