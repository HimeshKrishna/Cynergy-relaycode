#himesh krishna 
z={'I':1,'V':5,'X':10,'C':100,'M':500,'D':1000}
print("Enter from within the given list ",z)
A=input("Enter the first numeral: ")
B=input("Enter the second numeral: ")
D=0
E=0
for i in range(len(A)):
        for j in z:
            if(A[i]==j):
                    D=D+z[j]
for i in range(len(B)):
        for j in z:
            if(B[i]==j):
                    E=E+z[j]
print("Numeric Equivalent of first numeral = ",D)
print("Numeric Equivalent of second numeral = ",E)
Z=D+E
print("Sum of both numerals = ",Z)
F=str(Z);
R=''
for i in F:
        for j in z:
                if i==z[j]:
                        for i in range(int(i)):
                                R=R+j
print(R)