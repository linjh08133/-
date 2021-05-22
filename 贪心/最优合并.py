def func(ls):##ls储存每个数组的长度
    ls.sort()
    res = 0
    cur1 = 0 ##cur1为已合并的数组长度，cur2为下一个要合并进来的
    for i in ls:
        cur2 = i
        res += cur1 + cur2 - 1##计算合并次数
        cur1 += cur2##更新已合并数组长度
    return res
ls = [2,3,1,5,4]
print(func(ls))