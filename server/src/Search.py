from DataType import *

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
        for attribute, value in vars(instance).items():
            if isinstance(value, str):
                found_positions = KMPSearch(keyword, value)
                if found_positions:
                    results.setdefault(instance, []).append((attribute, len(found_positions)))
            elif isinstance(value, list) or isinstance(value, set):
                for item in value:
                    if isinstance(item, str):
                        found_positions = KMPSearch(keyword, item)
                        if found_positions:
                            results.setdefault(instance, []).append((attribute, len(found_positions)))
    return results
