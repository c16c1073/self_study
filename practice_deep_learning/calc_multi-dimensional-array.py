# p53
import numpy as np


print("------まずは、一次元（横一列）---------------")


A=np.array( [1,2,3,4] )
print(A)
print( np.ndim(A) )      # ndim で次元数を取得
print( A.shape )         # 配列の形状はインスタンス変数のshapeから取得できる
print( A.shape[0] )


print("------次は、2次元( 3*2の配列、縦3横2 ) ---------------")

B=np.array( [[1,2],[3,4],[5,6]] )
print(B)
print( np.ndim(B) )
print( B.shape )
print( B.shape[0] )


print("-----行列の内積------")


A2=np.array( [ [1,2],[3,4] ] )
B2=np.array( [ [5,6],[7,8] ] )
print(A2.shape) 
print(B2.shape)
print( np.dot(A2,B2) )  # 内積は”　ドット積　”とも言う
print("")
A3=np.array( [ [1,2,3],[4,5,6] ] )
B3=np.array( [ [1,2],[3,4],[5,6] ] )
print( A3.shape )
print( B3.shape )
print( np.dot(A3,B3) )









