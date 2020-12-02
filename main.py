import numpy as np

matrixA = np.array([[2,5,1,2,-1],[-2,0,3,5,7],[1,0,-1,1,3],[0,5,4,7,4]])
#A=np.matrix([[3,-2,5,0],[4,5,8,1],[1,1,2,1],[2,7,6,5]]).astype(float)
A=np.matrix([[2,5,1,2],
             [-2,0,3,5],
             [1,0,-1,1],
             [0,5,4,7]]).astype(float)
b=np.matrix([[-1],[7],[3],[4]]).astype((float))
#b=np.matrix([[2],[4],[5],[7]]).astype(float)
print("Duotoji matrica:")
print(A)
print("------------")
#print(b)
n=(np.shape(A))[0]
A1=np.hstack((A,b))
count=0
#tiesioginis etapas


#is youtube paimtas

for k in range (0, n-1):
    for i in range(k+1, n):
        if(A[i,k] == 0):
            i +=1
            print("i padidinam per viena")
        if(A[i,k] == 0):
            {
                print("Dalyba iš nulio negalima, sprendinių nėra.")

            }
        else:
            factor = A[k,k]/A[i,k]
        for j in range(k,n):
            A[i,j] = A[k,j]-A[i,j]*factor
            print()
        b[i] = b[k]-b[i]*factor
        print(A)
        print()
        print(b)
print(A)
print(b)

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