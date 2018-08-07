# p.45~
import numpy as np
import matplotlib.pylab as plt


def step_func(x):    # 引数ｘは実数（浮動小数点）しか入力することができない
    if x>0:
            return 1
    else :
            return 0

print( step_func(1) )
print( step_func(0) )

# 実際にはNUMPY配列を使って計算するので、以下のやり方がある
print("--------------numpyの配列を引数に取るには、、、↓　-------------------")

x=np.array( [-10,1.0,2.0] )


def step_func2(x):
    y=x>0                   # x>0でTrue,x<0でFalse(bool型)に変換した配列にする
    return y.astype( np.int )#int型に変換するときbool型の時は1か0に変換される
print( step_func2(x) )

print( "-----------------なにがおきていかというと、、、-----------------" )


y=x>0
print(y)  # "←　yの要素の型は、ブーリアン。ほしいのはint型の0か1")
y=y.astype( np.int )# y はyについてnumpy配列の型の変換をするよ、int型へ
print(y)



print("---------- graph of function -------------------")


#import matplotlib as plt

def step_func2(x2):
    return np.array( x2>0, dtype=np.int )# np.array( 配列の内容、dtype=配列の要素の型 )

x2=np.arange( -5.0,5.0,0.1 ) # ｘ軸は-5から5まで0.1刻みで出力
y2=step_func2(x2)

plt.plot(x2,y2)
plt.ylim(-2,2)
plt.show()












