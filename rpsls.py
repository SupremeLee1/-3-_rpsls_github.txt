#coding:gbk
"""
���RPSLS��Ϸ
���ߣ�������
"""

import random #����randomģ��
nike=random.randint(0,5)#����randint��������0-5֮����������
aj=input("���������ѡ��")
ʯͷ=0
ʷ����=1
��=2
����=3
����=4

def rpsls(aj):
	if aj==0 and (nike==3 or 4):
		print("��Ӯ��")
	if aj==1 and (nike==0 or 4):
		print("��Ӯ��")
	if aj==2 and (nike==1 or 0):
		print("��Ӯ��")
	if aj==3 and (nike==2 or 1):
		print("��Ӯ��")
	if aj==4 and (nike==3 or 2):
		print("��Ӯ��")
	if nike==0 and (aj==3 or 4):
		print("����Ӯ��")
	if nike==1 and (aj==0 or 4):
		print("����Ӯ��")
	if nike==2 and (aj==1 or 0):
		print("����Ӯ��")
	if nike==3 and (aj==2 or 1):
		print("����Ӯ��")
	if nike==4 and (aj==3 or 2):
		print("����Ӯ��")
	else:
		print("Error: No Correct Name")

print("���ѡ��Ϊ",aj)
print("������ѡ��Ϊ",nike)
rpsls(aj)
