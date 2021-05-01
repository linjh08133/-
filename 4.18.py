import re
import numpy as np
m1 = re.findall(r"^The[1-9]{4,11}","The32321The22321")
print(m1)




##列表生成式,中括号内写入for循环，对一个列表进行遍历，然后写一个if条件判断，对每次循环取出的值进行判断，结果为True的话将当前遍历到的值写入到新生成的列表中。
w = np.array([2,3,1])
wl = [np.zeros((x,y)) for (x, y) in zip(w[:-1],w[1:])]
print(wl)
x = [1,3,422]
x = np.array(x)
x1 = [xi for xi in x if xi >190]
print(x1)##筛选出大于190的，相当于np的where函数如下
x1 = np.array(x1)
print(x1[np.where(x1>190)])##where函数输出的是下标（只有1个参数时）
print(np.where(x<190,x,0))