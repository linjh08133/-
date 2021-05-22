class edge():
    def __init__(self,node1,node2,weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

def get_edge(ls):
    edgelist = []
    for i in ls:
        edgelist.append(edge(i[0],i[1],i[2]))
    return edgelist

class union_find():
    def __init__(self,n):
        self.root_index = [-1 for i in range(n)]
        print(self.root_index)

    def findroot(self,node):
        while(self.root_index[node] != -1):
            node = self.root_index[node]
        return node

    def union(self,node1,node2):##默认将node2当做根节点
        root1 = self.findroot(node1)
        root2= self.findroot(node2)
        self.root_index[root1] = root2
    def is_same_root(self,node1,node2):
        root1 = self.findroot(node1)
        root2 = self.findroot(node2)
        return root1 == root2




def kruskal(ls):##ls是边的列表，
    ls.sort(key = lambda x:x.weight)##对边升序排序
    ans_list = []
    u = union_find(9)
    n = 9
    for i in ls:##从最小边开始，选边构成生成树，如果这条边的2个顶点在同一树上，则舍弃

        if(not u.is_same_root(i.node1,i.node2)):
            ans_list.append((i.node1,i.node2))
            u.union(i.node1,i.node2)
        else:
            continue
        if(len(ans_list) == n-1):##边够了就不用再找了
            break
    return ans_list



ls = [[0,1,4],[0,7,8],[1,2,8],[1,7,11],[2,3,7],[2,5,4],[3,4,9],[3,5,14],[4,5,10],[5,6,2],[6,7,1],[6,8,6],[7,8,7],[2,8,2]]
edgelist = get_edge(ls)
ans = kruskal(edgelist)
for i in range(len(ans)):##转化成字母
    j = chr(ord("A")+ans[i][0]),chr(ord("A")+ans[i][1])
    ans[i] = j
print(ans)


