# p.57
import numpy as np


print("-----------neural network の内積------------")
print("--------入力2つで3つ出力、1層、バイアスと活性化関数は無視--------")

x=np.array( [1,2] )
print(x)
print( x.shape )

w=np.array( [ [1,3,5],[2,4,6] ] )
print( w )
print( w.shape )

y=np.dot(x,w)    # この計算結果である、3つの要素が出力である
print(y)         # もしdot関数を使わないと、一つずつ取り出すか、if,for 文を使う羽目になる


print("-------三層のneural network( 入力2つ、隠層3つ→2つ、出力2つ )-------")


# A1=X*w1+B1 の形にする
X=np.array( [1.0,0.5] )
w1=np.array( [ [0.1,0.3,0.5],[0.2,0.4,0.6] ] )
B1=np.array( [0.1,0.2,0.3] )

A1=np.dot(X,w1)+B1
print( A1 )


print("-----------0層から一層への伝達。計三層で活性化関数を導入------------")


def sigmoid(X):                 # 活性化関数はシグモイド関数
    return 1/( 1+np.exp(-X) )

z1=sigmoid(A1)
print( z1 )


print("-----------1層から2層への伝達。計三層で活性化関数を導入------------")


w2=np.array( [ [0.1,0.4],[0.2,0.5],[0.3,0.6] ] )
B2=np.array( [0.1,0.2] )

A2=np.dot(z1,w2)+B2
print( A2 )
z2=sigmoid( A2 )
print(z2)


print("------------出力層へ-------------")


def identity_function(x):  # 特に意味はないが、今までの流れを組んで書いておいた
    return x               # 恒等式（入力をそのまま出力）という。

w3=np.array( [ [0.1,0.3],[0.2,0.4] ] )
B3=np.array( [0.1,0.2] )

A3=np.dot( z2,w3 )+B3
y=identity_function(A3)
print(A3)
print(y)


print("------- まとめ  (neural network のfoword 方向への実装)---------")


def init_network(  ):  # 重みとバイアスの初期化、それらをディクショナリ型の変数networkに格納。
                       # 変数networkにはそれぞれの層で必要なパラメータ（重みとバイアス）が格納されている
    network={}
    network['w1']=np.array( [ [0.1,0.3,0.5],[0.2,0.4,0.6] ] )
    network['b1']=np.array( [ 0.1,0.2,0.3 ] )
    network['w2']=np.array( [ [0.,0.4],[0.2,0.5],[0.3,0.6] ] )
    network['b2']=np.array( [ 0.1,0.2 ] )
    network['w3']=np.array( [ [0.1,0.3],[ 0.2,0.4] ] )
    network['b3']=np.array( [ 0.1,0.2 ] )

    return network

def foward(network,x2):
    w1,w2,w3=network['w1'],network['w2'],network['w3']
    b1,b2,b3=network['b1'],network['b2'],network['b3']

    a1=np.dot(x2,w1)+b1
    z1=sigmoid(a1)     # 35行目に定義

    a2=np.dot(z1,w2)+b2
    z2=sigmoid(a2)

    a3=np.dot(z2,w3)+b3
    Y=identity_function(a3)   # 57行目に定義
    
    return Y

network=init_network()
x2=np.array([1.0,0.5])    # 初めの入力
Y=foward( network,x2 )
print(Y)














