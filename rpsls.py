#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
    if name=="ʯͷ":
	    number=0
    if name=="ʷ����":
	    number=1
    if name=="��":
	    number=2
    if name=="����":
	    number=3
    if name=="����":
	    number=4
    elif name!=("ʯͷ" or "ʷ����" or "��" or "����" or "����"):
	    number=5
    return number


def number_to_name(number7):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    
    if number7==0:
	    name7="ʯͷ"
    if number7==1:
	    name7="ʷ����"
    if number7==2:
	    name7="��"
    if number7==3:
	    name7="����"
    if number7==4:
	    name7="����"
    return name7


def rpsls(number7):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    number=name_to_number(name)
    number7=random.randint(0,5)#����randint��������0-5֮����������
    
    
    if number==0 and (number7==3 or 4):
	    print("��Ӯ��")
    elif number==1 and (number7==0 or 4):
	    print("��Ӯ��")
    elif number==2 and (number7==1 or 0):
	    print("��Ӯ��")
    elif number==3 and (number7==2 or 1):
	    print("��Ӯ��")
    elif number==4 and (number7==3 or 2):
	    print("��Ӯ��")
    elif number7==0 and (number==3 or 4):
	    print("����Ӯ��")
    elif number7==1 and (number==0 or 4):
	    print("����Ӯ��")
    elif number7==2 and (number==1 or 0):
	    print("����Ӯ��")
    elif number7==3 and (number==2 or 1):
	    print("����Ӯ��")
    elif number7==4 and (number==3 or 2):
	    print("����Ӯ��")
    elif number==5:
	    print("Error: No Correct Name")
   

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�



# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
name=input()
print("----------------")
number7=number7=random.randint(0,5)#����randint��������0-5֮����������
rpsls(number7)
name7=number_to_name(number7)
print("����ѡ��Ϊ:%s"%name)
print("�������ѡ��Ϊ:%s"%name7)
