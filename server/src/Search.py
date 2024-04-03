from DataType import *
from Recommend import *
from Route_select import *

# KMP算法用于模式搜索
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    # 创建lps[]将会为模式持有最长的前缀后缀值
    lps = [0]*M
    j = 0 # pat[]的索引
    # 预处理模式（计算lps[]数组）
    computeLPSArray(pat, M, lps)
    i = 0 # txt[]的索引
    results = []
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            results.append(i-j)
            j = lps[j-1]
        # j个匹配后的不匹配
        elif i < N and pat[j] != txt[i]:
            # 不匹配lps[0..lps[j-1]]字符,
            # 它们将 anyway 匹配
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return results

def computeLPSArray(pat, M, lps):
    len = 0 # 前一个最长前缀后缀的长度
 
    lps[0] = 0 # lps[0]始终为0
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

# 函数在类实例的文本属性中搜索关键字
def search_keyword_in_classes(keyword, instances):
    results = {}
    for instance in instances:
        total_occurrences = 0
        for attribute, value in vars(instance).items():
            if isinstance(value, str):
                found_positions = KMPSearch(keyword, value)
                if found_positions:
                    occurrences = len(found_positions)
                    total_occurrences += occurrences
                    if instance not in results:
                        results[instance] = []  # 确保此处已初始化
                    results[instance].append((attribute, occurrences))
            elif isinstance(value, list) or isinstance(value, set):
                for item in value:
                    if isinstance(item, str):
                        found_positions = KMPSearch(keyword, item)
                        if found_positions:
                            occurrences = len(found_positions)
                            total_occurrences += occurrences
                            if instance not in results:
                                results[instance] = []  # 确保此处已初始化
                            results[instance].append((attribute, occurrences))
        results[instance] = total_occurrences  # 使用总出现次数更新实例

    # 根据关键字出现的总次数对结果进行排序
    # 将字典转换为元组的列表，对其进行排序，如果需要，再转换回字典
    sorted_results = sort(results.items(), key="", mode=0)
    # 如果需要将排序后的结果作为字典：
    sorted_results_dict = dict(sorted_results)
    return sorted_results_dict

comment2 = Comment("Bob", ["Not as expected"], 2, time.localtime(time.time()))
journal2 = journal("Weekend Getaway", 3.0, ["Short trip", "Okayish experience"], {comment2}, time.localtime(time.time()))
keyword_results = search_keyword_in_classes("Not", [comment2, journal2])
print(keyword_results)