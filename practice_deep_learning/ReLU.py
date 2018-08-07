import numpy as np

def relu(x):
    return np.maximum(0,x)


x=[ 1,-2,3 ]

print( relu(x) )


'''
maximum関数は例えば、[ max(1,0),max(-2,0),max(3,0) ] を出力したいときは、np.maximum( x,0 )


'''
