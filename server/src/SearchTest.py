from Search import *

# 测试用例设置
comment1 = Comment("Alice", ["Great place"], 5, time.localtime(time.time()))
journal1 = journal("Trip to Paris", 4.5, ["Beautiful city", "Great food"], {comment1}, time.localtime(time.time()))
instances = [comment1, journal1]

# 测试用例1
keyword_results = search_keyword_in_classes("Great", instances)
assert len(keyword_results) == 2, "测试用例1失败"

# 测试用例2
keyword_results = search_keyword_in_classes("Alice", instances)
assert len(keyword_results) == 1 and len(keyword_results[comment1]) == 1, "测试用例2失败"

# 测试用例3
keyword_results = search_keyword_in_classes("city", instances)
assert len(keyword_results) == 1 and len(keyword_results[journal1]) == 1, "测试用例3失败"

# 测试用例4
keyword_results = search_keyword_in_classes("food", instances)
assert len(keyword_results) == 1 and len(keyword_results[journal1]) == 1, "测试用例4失败"

# 测试用例5
keyword_results = search_keyword_in_classes("missing", instances)
assert len(keyword_results) == 0, "测试用例5失败"

# 测试用例6
# 注意：假设我们已经在函数中适当处理了非字符串和非列表/集合属性
comment2 = Comment("Bob", ["Not as expected"], 2, time.localtime(time.time()))
journal2 = journal("Weekend Getaway", 3.0, ["Short trip", "Okayish experience"], {comment2}, time.localtime(time.time()))
keyword_results = search_keyword_in_classes("Not", [comment2, journal2])
assert len(keyword_results) == 1, "测试用例6失败"

print("所有测试用例通过。")