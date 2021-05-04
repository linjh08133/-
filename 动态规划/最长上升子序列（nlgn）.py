##贪心+二分
##贪心是每遇到一个数，就将其替代dp数组中第一个比他大的数，为的是让递增序列递增的越少越好
##dp数组是单调递增序列，所以可以二分查找

def serach(lis,x):##找第一个比x大的数，这里直接拿上一章作业的
    low = 0
    high = len(lis)
    low_index = 0
    high_index = len(lis)
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
    return high_index
def replace(ls,x):
    index = serach(ls,x)
    ls[index] = x


def func1(ls):##
    dp = [ls[0]]##dp数组是一个单调增序列
    for i in range(1,len(ls)):
        if(ls[i] > dp[-1]):##大于最后一个数就直接插在最后
            dp.append(ls[i])
        else:
            replace(dp,ls[i])##否则和dp数组中的第一个比他大的数替换
    return dp , len(dp)

print(func1([2,3,1,4,5,7,-1,0,8,7]))
