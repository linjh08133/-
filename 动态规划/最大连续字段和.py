
def calculate(ls):
    res, cur = 0, 0
    left = 0
    cur_left = 0
    right = 0
    for i in range(len(ls)):
        if cur + ls[i] < 0:##相加后小于0，这部分肯定不是最大值序列的一部分，直接舍弃,同时更新cur_left
            cur = 0
            print("t")
            cur_left = i+1
            continue
        if cur + ls[i] > res:##相加后大于最大值就更新,
            res = cur + ls[i]
            left = cur_left
            right = i+1

        cur += ls[i]##不管是不是答案的最大值，都要记录到cur中，因为是连续序列

    return res,ls[left:right]
ls = [15,-8,-2,7, 5, -11,17]
print(calculate(ls))