from src.DataType import *

'''
## @note 排序算法
## @param array 对象列表
## @param key 排序关键字(字符串格式)
## @param mode 排序方式(0:升序,1:降序)
## @return 排序后的对象列表(原列表不变)
'''
def quicksort(array,key:str):
    if len(array) <= 1:return list(array)
    array = list(array)
    base = getattr(array[0],key)
    left = [x for x in array[1:] if getattr(x,key) < base]
    right = [x for x in array[1:] if getattr(x,key) >= base]
    return quicksort(left,key) + [array[0]] + quicksort(right,key)

def sort(array,key:str,mode:int = 0):
    array = list(array)
    if len(array) <= 1:return list(array)
    try:
        getattr(array[0],key)
    except AttributeError as e:
        raise AttributeError('AttributeError:element {} is not exist'.format(key)) from e
    if mode == 0:return quicksort(array,key)
    else:return list(reversed(quicksort(array,key)))
