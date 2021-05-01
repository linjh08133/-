import random
def QuickSort(ls,left,right):
    if(left>=right):
        return  ls


    low,high = left,right
    a = ls[low]
    while(left<right):
        while(left<right and ls[right] >= a) :
            right-= 1
        while(left<right and ls[left] <= a):
            left += 1
        if(left<right):
            ls[right],ls[left] = ls[left],ls[right]
    ls[right],ls[low]=ls[low],ls[right]

    QuickSort(ls,low,left-1)
    QuickSort(ls,left+1,high)

def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])
ls = [random.randint(1,222) for i in range(13)]
print(ls)
QuickSort(ls,0,len(ls)-1)
print(ls)

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
reg = linear_model.RidgeCV(alphas=[0.1,1,10])
x = np.array([[2],[3],[4],[5]])
y = np.array([3.4,4.4,5.3,7.5])+np.random.rand(4)*20
print(y)
reg.fit(x,y)
k = reg.coef_
b = reg.intercept_
x1 = np.arange(0,10,0.2)
y1 = k * x1 + b
print(reg.alpha_)
plt.scatter(x,y)
plt.plot(x1,y1)
plt.show()