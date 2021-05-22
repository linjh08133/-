def activity_arrangement(ls):## 参数是一个n*2数组，[i][0]为开始时间，[i][1]为结束时间
    ls.sort(key = lambda x:x[1])##先按结束时间升序排序，sort函数默认是升序排序
    activity_list = [ls[0]]##第一个结束时间最早，根据贪心原则一定在解中
    count = 1
    m = 2
    while(m < len(ls)):
        if(ls[m][0] > activity_list[-1][1]):##假如活动开始时间在上个活动结束时间之后就可以加入
            activity_list.append(ls[m])     ##且因为经过了排序，这个时间的结束时间一定是剩下的活动中最早的
            count += 1
        m = m + 1
    return activity_list , count

def version2(ls):##按开始时间降序排序
    ls.sort(key = lambda x:x[0],reverse = True)
    print(ls)
    ans_list = [ls[0]]
    count = 1
    m = 2
    while( m < len(ls)):
        if(ls[m][1] <= ans_list[-1][0]):
            ans_list.append(ls[m])
            count += 1
        m += 1
    return ans_list

ls = [[0,6],[1,4],[3,5],[8,12],[3,8],[12,14],[8,11],[5,7],[6,10],[2,13]]
print(version2(ls))
print(activity_arrangement(ls))