from DataType import *
from typing import Iterable, Sequence, Any
'''
@note 排序算法
@param array 对象列表
@param key 排序关键字(字符串格式)
@param mode 排序方式(0:升序,1:降序)
@return 排序后的对象列表(原列表不变)
'''


def quicksort(array, key: str, compare):
  if len(array) <= 1:
    return list(array)
  array = list(array)
  base = getattr(array[0], key)
  left = [x for x in array[1:] if compare(base, getattr(x, key)) == False]
  right = [x for x in array[1:] if compare(base, getattr(x, key)) == True]
  return quicksort(left, key, compare) + [array[0]] + quicksort(right, key, compare)


def sort(array, key: str, compare):
  array = list(array)
  if len(array) <= 1:
    return list(array)
  try:
    getattr(array[0], key)
  except AttributeError as e:
    raise AttributeError(
        'AttributeError:element {} is not exist'.format(key)) from e
  return quicksort(array, key, compare)


def test_sort():
  test = [Building((0, 0), set(), "d", 0), Building((0, 0), set(), "v", 1), Building(
      (0, 0), set(), "b", 2), Building((0, 0), set(), "a", 3)]
  expected_result = [Building((0, 0), set(), "a", 3), Building((0, 0), set(
  ), "b", 2), Building((0, 0), set(), "d", 0), Building((0, 0), set(), "v", 1)]
  result = sort(test, "building_name", lambda x, y: x < y)
  for x in range(0, 4):
    print(result[x].building_name)
  return
