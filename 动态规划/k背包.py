##dp的算法没想出，贪心＋回溯的就可以
##先将数组降序排序，每一次都拿最大的进去，然后去深度，若大了就回溯，拿第二大的，以此类推
def kpack(ls,k,ans_list,end_index):
    global res
    if(k == 0):
        new_ans = ans_list.copy()##得复制了，要不然都指向同一对象
        res.append(new_ans)
        return
    if(k< 0):
        return

    for i in range(len(ls)):
        ans_list.append(ls[i])
        k -=ls[i]
        ls2 =  ls[i+1:]
        kpack(ls2,k,ans_list,end_index)
        ans_list.pop()##回溯步骤
        k +=ls[i]
        if(i == end_index):##最外层的遍历完了，就可以return了
            print(res)
            return res

def k_package(ls,k):##辅助函数，先把ls排序好
    ls.sort(reverse=True)
    print(ls)
    ans_list = []
    end_index = len(ls)-1
    res =[]
    kpack(ls,k,ans_list,end_index)

res = []

res = k_package([1,2,3,5,4,7,10],10)