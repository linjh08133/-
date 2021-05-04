import numpy as np
def mindis(ls):
    n = len(ls)
    dp = ls.copy()
    for d in range(2,n):##第一条斜对角线的不用去遍历了，因为i到i+1只有1种方式,ls也已经记录了
        for i in range(0,n-d):
            j = d+i
            min = ls[i][j]
            for k in range(1,d):
                if(min > dp[i][k] + dp[k][j]):
                    dp[i][j] = dp[i][k] + dp[k][j]
ls = [[0,1,4,6],[1,0,2,3],[4,2,0,3],[6,3,3,0]]
mindis(ls)