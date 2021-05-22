import numpy as np
def check(cur):
    n = len(cur)
    for i in range(n-1):
        if cur[i] == cur[-1] or abs(cur[i] - cur[-1]) == abs(i - n + 1)  :##如果值相同就是在同一行，
            ##如果后面那个等式成立就是在同一对角线了，注意距离要用绝对值表示
            return False
    return True
def dfs(ls,anslist,cur,n):
    if(len(cur) == n):
        ans = cur.copy()
        anslist.append(ans)
        return
    for i in range(n):
        cur.append(i)
        if(check(cur) == False):##与规则不符直接删除进入当前层的下一种可能
            del cur[-1]
            continue
        else:
            dfs(ls,anslist,cur,n)##遍历
            del cur[-1]##回溯操作


    return anslist





def n_queen(n):
    ls = np.zeros(n)
    anslist = []##储存答案的
    cur = []##储存当前遍历的子集
    anslist = dfs(ls,anslist,cur,n)
    count = len(anslist)
    return anslist,count

print(n_queen(9)[1])
