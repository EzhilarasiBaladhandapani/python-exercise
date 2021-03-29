A = "hello have a awesome day"
n = A.find('have')
b = A.find('day')
if  b > n:
    A = A.replace(A[n:(b+3)],'everyone')
    print(A)