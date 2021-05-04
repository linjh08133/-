def QuickSort(ls,left,right):
    if(left>=right):
        return  ls


    low,high = left,right
    a = ls[low]
    while(left<right):##左右跳坑法
        while(left<right and ls[right] >= a) :
            right-= 1
        ls[left]=ls[right]##仍给左的

        while(left<right and ls[left] <= a):
            left += 1
        ls[right]= ls[left]##扔给右的

    ls[right ] = a##相遇了，将pivot赋值给相遇的那个点
    QuickSort(ls,low,left-1)
    QuickSort(ls,left+1,high)

ls = [0,2,1,4,2,66,12,45,11,221,25,17]
print(QuickSort(ls,0,len(ls)-1))
print(ls)