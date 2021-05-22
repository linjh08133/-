import numpy as np
def dijkstra(matrix):
    ##邻接矩阵[0][0],表示a到a的距离，其他类似，[i][i]默认为0，若没有连接边则为无穷
    visited = []##记录访问过的点
    min_dis = [float("inf") for i in range(len(matrix))]##初始化距离，在没有访问任何点时距离为无穷大
    visited.append(0)##默认找第一个点到其他点最小距离，想找其他点到其他点的距离只需要加个for迭代就好
    min_dis = matrix[0]
    for i in range(len(matrix) - 1):##要访问剩下的n-1个点
        print(min_dis)
        m = float("inf")
        index = 1
        for j in range(1,len(matrix)):##找到最近的那个点，且改点未被访问过，根据贪心原则，这个就是最优解
                if(min_dis[j] < m and j not in visited):
                    index = j
                    m = min_dis[j]
        visited.append(index)##访问改点了
        for k in range(1,len(matrix)): ##如果原来访问过的点到该点的距离，加上这个点到剩下的未访问点的距离小于原来点到剩下的未访问距离，就更新min_dis
            if(k not in visited and min_dis[index] + matrix[index][k] < min_dis[k]):
                min_dis[k] = min_dis[index] + matrix[index][k]

def get_matrix(n,l):
    ls = [float("inf") for i in range(n)]
    matrix = [ls.copy() for i in range(n)]##不能直接ls去组成每一行的元素，这样每一行实际上指向同一个对象
    for i in range(n):
        matrix[i][i] = 0
    for i in l :
        matrix[i[0]][i[1]] = i[2]
    return matrix
l = [[0,1,20],[0,2,38],[1,0,9],[1,2,15],[1,3,37],[2,4,5],[2,3,18],[3,1,15],[3,5,13],[4,3,11],[4,5,8],[5,2,19],]
matrix = get_matrix(6,l)
dijkstra(matrix)