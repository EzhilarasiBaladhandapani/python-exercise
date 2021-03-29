A = "string"
length = len(A)
if len(A) >=3:
    if A[-3:] == "ing":
        print(A[0:-3] + "ly")
    else:
        print(A + "ing") 
else:
    print(A)  