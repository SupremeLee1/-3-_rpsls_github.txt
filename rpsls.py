#coding:gbk
"""
完成RPSLS游戏
作者：李莲秋
"""

import random #调用random模块
nike=random.randint(0,5)#利用randint方法产生0-5之间的随机整数
aj=input("请输入你的选择")
石头=0
史波克=1
布=2
蜥蜴=3
剪刀=4

def rpsls(aj):
	if aj==0 and (nike==3 or 4):
		print("你赢了")
	if aj==1 and (nike==0 or 4):
		print("你赢了")
	if aj==2 and (nike==1 or 0):
		print("你赢了")
	if aj==3 and (nike==2 or 1):
		print("你赢了")
	if aj==4 and (nike==3 or 2):
		print("你赢了")
	if nike==0 and (aj==3 or 4):
		print("机器赢了")
	if nike==1 and (aj==0 or 4):
		print("机器赢了")
	if nike==2 and (aj==1 or 0):
		print("机器赢了")
	if nike==3 and (aj==2 or 1):
		print("机器赢了")
	if nike==4 and (aj==3 or 2):
		print("机器赢了")
	else:
		print("Error: No Correct Name")

print("你的选择为",aj)
print("机器的选择为",nike)
rpsls(aj)
