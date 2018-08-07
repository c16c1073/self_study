# p48
import numpy as np
import matplotlib.pylab as plt



def sigmoid(x):
    return 1/( 1+np.exp(-x) )

x=np.array([ -1.0,1.0,2.0 ])
print( sigmoid(x) )


print("-----↓　スカラ値とNUMPY配列での演算が行われると、スカラ値とNUMPY配列の各要素同士で演算が行われる↓ ----")


t=np.array( [1.0, 2.0, 3.0] )
print(  t+1 )


print("------------------------------------")


x=np.arange( -5,5,0.1 )
y=sigmoid(x)

plt.ylim(-1.0,2.0)
plt.plot(x,y)
plt.grid()
plt.show()















