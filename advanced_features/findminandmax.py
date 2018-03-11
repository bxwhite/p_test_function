# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return (None,None)
    min = L[0]
    max = L[-1]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min,max)

print(findMinAndMax([]))