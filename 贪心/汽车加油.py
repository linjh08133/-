def serach(lis,x):##找第一个比x小的数，这里直接拿上一章作业的
    low = 0
    high = len(lis)
    low_index = 0
    high_index = len(lis)
    if(x > lis[-1]):
        return len(lis)-1
    if(len(lis) == 0):##空表
        return 0
    if(x < lis[0]):##特殊情况的处理
        return 0
    while(low <= high):
        mid = int((low + high) / 2)
        if( lis[mid] == x):
            low_index = high_index = mid
            return mid
        elif (lis[mid] > x):
            high = mid - 1
            high_index = mid
        else:
            low = mid + 1
            low_index = mid
    return low_index


def gas(ls,n,des):##ls是每个加油站距离起始点的位置，n是加满一次油走的距离
    times = 0
    index = serach(ls,n)
    cur = 0
    ans_list = []
    while (cur + n < des):##没跑到终点
        index = serach(ls, cur + n)
        times += 1
        ans_list.append(ls[index])
        cur = ls[index]##跑到这个加油站
    return times,ans_list

ls = [3,5,7,8,9,13,14]
print(gas(ls,5,16))