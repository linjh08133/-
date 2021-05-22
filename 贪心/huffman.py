class Node ():
    def __init__(self,Name=None,value =None):##这是一个节点
        self.value = value
        self.name = Name
        self.left = None
        self.right = None
##heapq不支持将node推入堆，我也没想出来怎么弄，就手写一个能推入node的二叉堆吧^^
##实现push和pop就够用了，
class heap_for_node():
    def __init__(self):
        self.ls = []
        self.length = 0
    def push (self,node):
        self.ls.append(node)
        self.length += 1
        cur_index = self.length-1
        while(cur_index > 0):
            parent_index = (cur_index-1) // 2
            if (self.ls[parent_index].value > self.ls[cur_index].value):
                self.ls[parent_index], self.ls[cur_index] = self.ls[cur_index], self.ls[parent_index]
                cur_index = parent_index
            else:
                break


    def pop (self):
        out = self.ls[0]
        self.length -= 1
        self.ls[0] = self.ls[self.length]
        del self.ls[self.length]
        cur_index = 0
        while(cur_index * 2 + 1 < self.length):
            min1 = self.ls[cur_index * 2 + 1].value
            min1_index = cur_index * 2 + 1
            if(cur_index * 2 + 2 < self.length and min1 > self.ls[cur_index * 2 + 2].value):
                min1 = self.ls[cur_index * 2 + 2].value
                min1_index = cur_index * 2 + 2
            if(min1 < self.ls[cur_index].value):
                self.ls[cur_index],self.ls[min1_index] = self.ls[min1_index], self.ls[cur_index]
                cur_index = min1_index
            else:
                break
        return out

def tree_spanning(ls):##ls列表是n*2数组，ls[i][0]是名字，ls[i][1]是频率
    heap = heap_for_node()
    for i in ls:##用ls构建堆,同时实例化对象
        node = Node(i[0],i[1])
        heap.push(node)
    while(heap.length > 1):##不断的取出最小的2个，再生成一个新结点，新结点左右子树就是这2个取出点
        left_node = heap.pop()
        right_node = heap.pop()
        new_node = Node(Name=left_node.name + "" + right_node.name,value=left_node.value + right_node.value)
        new_node.left = left_node
        new_node.right = right_node
        heap.push(new_node)
    return heap.ls[0]
def get_code(root,code):##其实就是中序遍历，先输出当前结点的编码，将这个编码加上0或1后遍历左右子树
    if( not root):
        return
    if(len(root.name) == 1):##忽略非叶子节点
        print("{}的编码是{}".format(root.name,code))
    get_code(root.left,code+"0")
    get_code(root.right,code+"1")
ls = [["a", 0.1], ["e", 0.15],["i", 0.12], ["t", 0.04], ["S", 0.03],["y",0.13],["z",0.01]]
root = tree_spanning(ls)
get_code(root,"")