#! /usr/bin/env python
# -*-coding:utf-8 -*-

import sys
import re

print('start proc')

file1='E:/python/CDH.log'
file2="E:/python/CDH_cnt.log"

with open(file1,'r') as f1:
	lines = f1.readlines()

for line in lines:
	if line.find('Calculating') != -1:
		with open(file2,'a+') as f2:
			print(line)
			f2.write(line)
for line in lines:
	if line.find('ROWS=') != -1:
		with open(file2,'a+') as f2:
			print(line)
			f2.write(line)			
