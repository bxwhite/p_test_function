# -*- coding: utf-8 -*- 
#方法1
def trim(s):
	i = 1
	if s == '':
		return s
	while i :
		if s[:1] == ' ':
			s = s[1:]
		else:
			break
	while i:
		if s[-1:0] == ' ':
			s = s[0:-1]
		else:
			break
	return s	
stri = " ABCDEF "
print(trim(stri))

#方法2
def trim_2(s):
	if s == '':
		return s
	else:
		while s[0:1] == ' ':
			s = s[1:]
		while s[-1:0] == ' ':
			s = s[:-1]
	return s
stri_2 = "  EFGHI  "
print(trim_2(stri_2))

#方法3 递归
def trim_3(s):
    if s == '':
        return s
    if s[0:1] == ' ':
        return s[1:]
    if s[-1:0] == ' ':
        return s[0:-1]
    return s
stri_3 = '  hello  '
print(trim_3(stri_3))

