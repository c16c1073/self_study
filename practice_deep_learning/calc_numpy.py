import numpy as np

x=np.array( [1.0,2.0,3.0] )    # x に np を使った配列を作る
y=np.array( [2.0,4.0,6.0] )

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x/2)

print("--------------------------------------------------------------------") #-------Numpy のN次元配列

A=np.array( [ [1,2],[3,4] ] )

print(A)
print(A.shape)
print(A.dtype)


B=np.array( [ [3,0],[0,6] ] )

print(A+B)
print(A*B)

print("--------------------------------------------------------------------") #-----access to index

X=np.array(  [ [51,55],[14,19],[0,4]  ]  )
print(X)
print(X[0])
print(X[2][1])

for row in X:
        print(row)

X=X.flatten()
print(X)
print(X[ np.array( [0,2,4] ) ])
print( X>15 )
print( X[X>15] )





