import numpy as np
import matplotlib.pyplot as plt
#import matplotlib as plt

# データの作成
x=np.arange(0,6,0.1)  #  0から6まで0.1刻みで生成
y=np.sin(x)

# グラフの描画
plt.plot(x,y)
plt.plot(y,x)
plt.show()

#----------------------------------------------------------------------------

y1=np.sin(x)
y2=np.cos(x)

plt.plot( x, 5*y1, label="sin" )
#plt.plot( x, 5*y2, linestyle="__", label="cos" )
plt.plot( x, 5*y2,  label="cos" )


plt.xlabel("X")
plt.ylabel("Y")
plt.title( 'sin & cos' )

plt.show()




