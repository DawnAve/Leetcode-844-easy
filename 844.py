def backspaceCompare(s,t) :
        A=B=[]
        for i in s:
            if A and i == "#":
                A.pop()
            else:
                A.append(i)
        print(A)
        for j in t:
            if B and j == "#":
                B.pop()
            else:
                B.append(j)
        
        print(B)
        print( A==B)
backspaceCompare("y#fo##f", "y#f#o##f")
