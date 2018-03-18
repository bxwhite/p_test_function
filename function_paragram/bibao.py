#利用可变的list:
def createCounter_2():
    n = [0]
    def counter():
        n[0] += 1
        return n[0]
    return counter


#利用nonlocal改变外部参数：
def createCounter_1():
    n = 0
    def counter():
        nonlocal n
        n+=1
        return n
    return counter
# 测试:
counterA = createCounter_1()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter_1()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')