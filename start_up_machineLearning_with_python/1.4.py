

















# 1.4.5  pandas
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

data = { 'name':["john","anna","peter","linda"],
         'location':["new york","paris","berlin","london"],
         'age':["24","13","53","33"]
         }
data_pandas=pd.DataFrame(data)
display(data_pandas)

display( data_pandas[ data_pandas.age>30 ] )













