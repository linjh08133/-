import numpy as np
def findzi(string1, string2):
    n,m = len(string1), len(string2)
    dp = np.zeros((n, m))
    string = []
    for i in range(1, n):
        for j in range(1, m):
            if (string1[i] == string2[j]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    print(string)
    return dp[n-1][n-1]

s1 = "GACCTGTG"
s2 = "CATACGGATFG"
print(findzi(s1,s2))