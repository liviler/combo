def sortPartitions(listObject):
    '''
    Sort the list by the length of 
    将列表及其子表的按照长度递增顺序调整顺序
    '''
    res=listObject
    if(len(res)>=1):
        res.sort(key=len,reverse=False)
        for i in res:
            i.sort(key=len,reverse=False)
    return res 

print(sortPartitions([[[1,2],[1,2,3],[1]]]))


def A(Low,Up)->list:
    return [[Low],[Up]]


print(A(1,2))
