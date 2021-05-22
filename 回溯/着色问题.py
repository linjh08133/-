def check(cur,ls):
    for i in range(len(cur)-1):
        if(ls[len(cur)-1][i] == 1 and cur[-1] == cur[i]):##检查是否有冲突的
            return False

    return True


def dfs(ls,cur,n,m,anslist):
    if (len(cur) == n):
        anslist.append(cur.copy())

        return
    for i in range(m):
        cur.append(i)
        if(check(cur,ls) == True):##剪枝看一下能不能走下去
            dfs(ls,cur,n,m,anslist)
        else:
            del cur[-1]##不能就删了这个进入该层的下一个可能
            continue
        del cur[-1]##回溯操作
    return anslist


def main(ls,n,m) :##ls是邻接矩阵，值为1时连接，0时不，m是最多颜色
    n = len(ls)
    cur = []
    anslist = []
    print(len(dfs(ls,cur,n,m,anslist)))


ls = [[1,1,0,1],[1,1,0,0],[0,0,1,1],[1,0,1,1]]
main(ls,4,3)