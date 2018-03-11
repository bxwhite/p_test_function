#去掉空字符串
def not_empty(s):
    return s and s.strip()
p = input('input:')
print(list(filter(not_empty, p)))
# 结果: ['A', 'B', 'C']