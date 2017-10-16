def bsearch(data, target):
    left=0
    right=len(data)-1
    while left<=right:
        mid=(left+right)//2
        if target<data[mid]:
            right=mid-1
        elif target>data[mid]:
            left=mid+1
        elif target==data[mid]:
            return mid
    else:
        return None


count=[1,5,6,8,11,13,15]
en=bsearch(count,11)
print(en)
