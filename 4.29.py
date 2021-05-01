from collections import  Counter
import numpy as np

x = np.random.randn(333,4)
mea = x.mean(axis=0)
var = x.var(axis=0)
print(mea)
print(var)