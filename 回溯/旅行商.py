import numpy as np
max = float("inf")
def dfs(ls,n,anslist,length,cur,choice):
    global max
    if(len(cur) == n):
        if(length<max):
            anslist = cur.copy()
            max = length
            print(max)
            print(anslist)
            return
    for i in range(len(choice)):
        cur.append(choice[i])
        if(length + ls[cur[-2]][choice[i]]  > max):
            del cur[-1]
            continue
        else:
            length += ls[cur[-2]][choice[i]]
            dfs(ls,n,anslist,length,cur,choice[:i]+choice[i+1:])
        del cur[-1]
        length -= ls[cur[-1]][choice[i]]





def main(n,ls):
    cur = [0]
    anslist = [0]
    max = float("inf")
    choice = [i for i in range(1,n)]
    length = 0
    dfs(ls,n,anslist,length,cur,choice)

ls= [[float("inf"),3,2,5],[3,float("inf"),6,4],[2,6,float("inf"),1],[5,4,1,float("inf")]]


fi = open("tsp.txt")
x = []
y = []
for line in fi:
    line = line.replace("\n","")
    line = line.split(" ")
    x.append(float(line[0]))
    y.append(float(line[1]))
x = np.array(x)
y = np.array(y)
n = len(x)
matrix = np.zeros((n,n))
for i in range(n) :
    for j in range(1,n):
        matrix[i][j] = ((x[i]-x[j])**2 + (y[i] - y[j])**2)**0.5

main(12,matrix[:12,:12])