import numpy as np
def func(ls):
    ##dp[i]表示的是以ls[i]结尾的子序列的最长长度
    dp = np.zeros(len(ls))
    for i in range(len(ls)):
        m = dp[0]
        for j in range(i):
            if (dp[j] > m and ls[j] < ls[i]):
                m = dp[j]
        dp[i] = m + 1
    return dp ,np.max(dp)
print(func([2,3,1,4,5,7,-1,0,8,7]))