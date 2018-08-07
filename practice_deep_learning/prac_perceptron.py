import numpy as np


def AND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7
    tmp=x1*w1+x2*w2
    if tmp <= theta:
            return 0
    elif tmp > theta:
            return 1

print( AND(0,0) )
print( AND(1,0) )
print( AND(0,1) )
print( AND(1,1) )


print("-----------------------------------------------")


def nand(x1,x2):
    w1,w2,theta=-0.5,-0.5,-0.7
    tmp=x1*w1+x2*w2
    if tmp <= theta:
            return 0
    elif tmp > theta:
            return 1

print( nand(0,0) )
print( nand(1,0) )
print( nand(0,1) )
print( nand(1,1) )


print("---------------------------------------------------")


def OR(x1,x2):
    w1,w2,theta=1,1,1
    tmp=x1*w1+x2*w2
    if tmp < theta:
            return 0
    elif tmp >= theta:
            return 1

print( OR(0,0) )
print( OR(1,0) )
print( OR(0,1) )
print( OR(1,1) )


print("------------- ↓ 重みとバイアス(下駄履き)の導入↓ -------------------")

# x*w+b=0 の形を目指す
x=np.array( [0,1] )        # 入力
w=np.array( [0.5,0.5] )    # 重み
b=-0.7                     # バイアス（これまでのthetaに-1をかけたやつ　）

print(w*x)              # 各要素が乗算される
print( np.sum(w*x) )    # 各要素を加算
print( np.sum(w*x)+b )  # 浮動小数点数による演算誤差を含む、およそ-0.2


print("---------------配列を使ったAND回路--------------------------")


def AND2(x1,x2):
    x=np.array( [x1,x2] )
    w=np.array( [0.5,0.5] )
    b=-0.7
    tmp = np.sum( w*x )+b
    if tmp<=0:
            return 0
    else:
         return 1

print( AND2(0,0) )
print( AND2(1,0) )
print( AND2(0,1) )
print( AND2(1,1) )





print("-------------------nandゲートとorゲート-------------------------")


def nand2(x1,x2):
    x=np.array( [x1,x2] )
    w=np.array( [-0.5,-0.5] )
    b=0.7
    tmp=np.sum(w*x)+b
    if tmp<=0:
            return 0
    else :
            return 1

print( nand2(0,0) )
print( nand2(1,0) )
print( nand2(0,1) )
print( nand2(1,1) )



print("--------------------------")


def OR2(x1,x2):
    x=np.array( [x1,x2] )
    w=np.array( [0.5,0.5] )
    b=-0.2
    tmp=np.sum(w*x)+b
    if tmp<=0:
            return 0
    else:
            return 1

print( OR2(0,0) )
print( OR2(1,0) )
print( OR2(0,1) )
print( OR2(1,1) )


print("--------------- xor回路-------------------------------------")


def xor(x1,x2):
    s1=nand2(x1,x2)
    s2=OR2(x1,x2)
    y=AND2(s1,s2)
    return y

print( xor(0,0) )
print( xor(1,0) )
print( xor(0,1) )
print( xor(1,1) )



























