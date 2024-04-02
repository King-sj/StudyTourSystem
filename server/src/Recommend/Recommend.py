from src.Data.DataType import *

'''
## @note 排序算法
## @param array 对象列表
## @param key 排序关键字(字符串格式)
## @param mode 排序方式(0:升序,1:降序)
## @return 排序后的对象列表(原列表不变)
'''
def sort(array,key:str,mode:int = 0):
    if len(array) <= 1:return list(array)
    try:
        array = list(array)
        base = getattr(array[0],key)
        left = [x for x in array[1:] if getattr(x,key) < base]
        right = [x for x in array[1:] if getattr(x,key) >= base]
        if mode == 0:return list(sort(left,key,mode) + [array[0]] + sort(right,key,mode))
        else:return list(reversed(sort(right,key,mode) + [array[0]] + sort(left,key,mode)))
    except AttributeError as e:
        raise AttributeError('AttributeError:element {} is not exist'.format(key)) from e


