def f(ls,m_weight):##懒得取名了,ls是重量的数组,m_weight是最大重量
    ls.sort()
    load_list =[]
    total = 0  ##记录当前重量
    cur = 0  ##记录走到哪个货物
    while(total < m_weight):
        if(ls[cur] + total < m_weight):
            load_list.append(ls[cur])
            total += cur
            cur +=1
        else :##超重了，直接结束
            break
    return  load_list

ls = [2,3,51,1,24,123,1,2,5,1,5,1]
print(f(ls,150))
