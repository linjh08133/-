##将n多边形
##𝑡(𝑖,𝑗)=𝑚𝑖𝑛{t(𝑘+1,𝑗)+𝑡(𝑖,𝑘)+𝑤_(𝑖−1,𝑘𝑗)}
import numpy as np

def calculate_w(i,j,k):
    return 0
def w (ls):
    n = len(n)
    dp = np.zeros((n+1,n+1))
    for d in range(2,n+1):
        for i in range (2,n-d+1):

