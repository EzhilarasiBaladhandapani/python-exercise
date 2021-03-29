A = "abcdef"
B =  "dhijk"
Alen = len(A)
Blen = len(B)

if Alen %2 ==0:
    Aindex = Alen//2
else:
    Aindex=(Alen//2)+1
if Blen % 2== 0:
    Bindex = Blen//2
else:
    Bindex = (Blen//2)+1

    Afront = A[0:Aindex]
    Aback = A[Aindex:]

    Bfront = B[0:Bindex]
    Bback = B[Bindex:]  
    print(Afront+Bfront+Bback+Aback)         
