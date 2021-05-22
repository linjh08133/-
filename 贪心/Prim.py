import numpy as np
def prim(ls):
    visted_list = set()##记录访问过的，用set
    visted_list.add(0)
    dis_list = np.array(ls[0])
    print(dis_list)
    dis_index = [0 for i in range(len(ls))]
    res = []
    for i in range(len(ls)-1):##要找n-1条边
        min_index = 0
        cur = float("inf")
        for j in range(1,len(ls)):##找n-1个点找到下一个加入的点
            if(dis_list[j] <cur and j not in visted_list):
                cur = dis_list[j]
                min_index = j
        visted_list.add(min_index)
        res.append((dis_index[min_index],min_index))
        for k in range(len(ls[min_index])):#3更新距离同时也要更新最短那个点的坐标
            if (dis_list[k] > ls[min_index][k] and k not in visted_list ):##进来一个点同时要更新到生成树的距离
                dis_list[k] = ls[min_index][k]
                dis_index[k] = min_index
        print(dis_list)
    print(res)
l = [float("inf") for i in range (9)]
ls = [[0, 4, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 8, float("inf")], [4, 0, 8, float("inf"), float("inf"), float("inf"), float("inf"), 11, float("inf")], [float("inf"), 8, 0, 7, float("inf"), 4, float("inf"), float("inf"), 2], [float("inf"), float("inf"), 7, 0, 9, 14, float("inf"), float("inf"), float("inf")], [float("inf"), float("inf"), float("inf"), 9, 0, 10, float("inf"), float("inf"), float("inf")], [float("inf"), float("inf"), 4, 14, 10, 0, 2, float("inf"), float("inf")], [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 2, 0, 1, 6], [8, 11, float("inf"), float("inf"), float("inf"), float("inf"), 1, 0, float("inf")], [float("inf"), float("inf"), 2, float("inf"), float("inf"), float("inf"), 6, float("inf"), 0]]
ls[7][8] = 7
ls[8][7] =7
print(ls)
prim(ls)


