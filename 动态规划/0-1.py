import  numpy as np
def package1(w,v,cap):
    w.insert(0, 0)
    v.insert(0, 0)
    print(w)
    dp = np.zeros((len(w), cap+1))
    for i in range(1,len(w)):
        for j in range(1,cap+1):
            if w[i] <= j:
                dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]

w=[2,3,5,6]
v=[3,4,5,7]
package1(w,v,11)
