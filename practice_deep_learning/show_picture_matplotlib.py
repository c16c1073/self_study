#  p18

import matplotlib.pyplot as plt
from matplotlib.image import imread


img=imread( 'S__14909447.jpg' )   # カレントディレクトリにファイルがあると、ファイル名を書く
plt.imshow(img)

plt.show()

