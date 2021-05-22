def dfs(cur,anslist,n,choice):
    if(len(cur) == n):
        anslist.append(cur.copy())
        print(cur)
        return
    for i in range(len(choice)):
        cur.append(choice[i])
        dfs(cur,anslist,n,choice[:i]+choice[i+1:])
        del cur[-1]
    return anslist


def npai(n):
    anslist = []
    cur = []
    choice = [i for i in range(1,n+1)]
    print(len(dfs(cur,anslist,n,choice)))
npai(25)