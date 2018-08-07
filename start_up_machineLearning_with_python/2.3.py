import matplotlib.pyplot as plt
import mglearn
# データセットの生成
x,y=mglearn.datasets.make_forge()

mglearn.discrete_scatter( x[:,0],x[:,1],y )
plt.show()



