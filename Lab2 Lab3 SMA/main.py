import numpy as np

A=np.matrix([[1,0,-1,1],
             [2,5,1,2],
             [-2,0,3,5],
             [0,5,4,7]]).astype(float)
b=np.matrix([[3],[-1],[7],[4]]).astype((float))
print("Duotoji matrica:")
print(A)
print("------------")
#print(b)
n=(np.shape(A))[0]
A1=np.hstack((A,b))
count=0
#tiesioginis etapas
SameElements =0
for k in range(n-1): #nuo 0 iki n-1 (mano atveju iki 4)
    for i in range(k+1,n):
        if A[i,k] == 0: continue
        factor = A[k,k]/A[i,k]
        count +=1
        print("--------------")
        print("Iteracija = {0}".format(count))
        print(factor)
        for j in range(k,n):
            A[i,j] = A[k,j] - A[i,j] * factor

        b[i] = b[k] - b[i]*factor
        print("{0}|\n{1}".format(A,b))
        print("-------------")
    for l in range(n-1):
        for j in range(n):
            if(A[l,j] == A[l+1,j]):
                SameElements+=1
                if(SameElements == n):
                    if(b[l] != b[l+1]):
                        print("Lygtys nesuderintos.")
                        exit("Matrica sprendiniu neturi.")
        SameElements = 0
print("{0}\n|{1}".format(A,b))
print("Atgalinis etapas")
# atgalinis etapas:
x=np.zeros(shape=(n,1))
print(x)


#is yt
x[n-1] = b[n-1]/A[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ax= 0
    for j in range(i+1, n):
        sum_ax+=A[i,j]*x[j]
    x[i]=(b[i] - sum_ax) / A[i,i]

print("Sprendiniai yra:")
print(x)