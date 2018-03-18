#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'module test'
_author_ = 'bai'

import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print('hello python')
	elif len(args) == 2:
		print('get, %s'% args[1])
	else: 
		print('too many words')
if __name__=='__main__':
	test()
