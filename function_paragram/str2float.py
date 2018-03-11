# -*- coding: utf-8 -*- 
from functools import reduce
def str2float(s):
    a,b = s.split(r'.')
    def fun(x,y):
        return x*10+y
    n1 = reduce(fun,map(int,a))
    temp = reduce(fun,map(int,b))
    n3 = temp/10**len(b)
    return n1+n3
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')