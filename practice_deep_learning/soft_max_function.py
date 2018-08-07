# p66
import numpy as np
import matplotlib.pylab as plt

a=np.array( [ 0.3,2.9,4.0 ] )
exp_a=np.exp(a)
print( exp_a )

sum_exp_a=np.sum(exp_a)   # 上のexp_aの各要素の和
print( sum_exp_a )

y=exp_a/sum_exp_a    # ソフトマックス関数の結果
print( y )


print( "------------関数化すると------------" )


def softmax(a):
    exp_a2=np.exp(a)
    sum_exp_a2=np.sum(exp_a2)
    Y=exp_a2/sum_exp_a2
    return Y
print( softmax(a) )
# このような指数関数をPC上で扱うときは簡単に値が大きくなり、こういう値どうしでの割り算は結果が不安定になる
# よって、softmax関数の改善案が下記である


print( "--------softmax関数改善--------" )


a2=np.array( [ 1010,1000,990 ] )
print( np.exp(a2)/np.sum(np.exp(a2)) )  # 正しく計算されない　nan=nor a number:不定
c=np.max(a2)  # 配列の中の最大値を返す
print(a2-c)
print( np.exp(a2-c)/np.sum(np.exp(a2-c) ) )  # 出力できた


print("--------実装すると-----------")


def softmax2(a2):
    c=np.max(a2)
    exp_a2_2=np.exp(a2-c)
    sum_exp_a2=np.sum(exp_a2_2)
    y2=exp_a2_2/sum_exp_a2
    return y2
print(softmax2(a2))

a3=np.array( [0.3,2.9,4.0] )
y3=softmax2(a3)
print(y3)



