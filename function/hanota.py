# -*- coding: utf-8 -*-
#汉诺塔问题
#算法可以分为三部
#1:把前n-1个从A-->B
#2:A-->C
#3:剩下n-1从B--C
def move(n,a,b,c):
	if(n==1):
		print(a'-->'c)
	else:
		move(n-1,a,c,b)
		print(a'-->'c)
		move(n-1,b,a,c)
	
move(3,'A','B','C')