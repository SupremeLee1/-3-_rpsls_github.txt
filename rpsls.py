#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random
numberC=random.randint(0,4)#����randint��������0-5֮����������

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(nameU):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
    if nameU=="ʯͷ":
	    numberU=int(0)
    if nameU=="ʷ����":
	    numberU=int(1)
    if nameU=="��":
	    numberU=int(2)
    if nameU=="����":
	    numberU=int(3)
    if nameU=="����":
	    numberU=int(4)
    return numberU


def number_to_name(numberC):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    
    if numberC==int(0):
	    nameC="ʯͷ"
    if numberC==int(1):
	    nameC="ʷ����"
    if numberC==(2):
	    nameC="��"
    if numberC==(3):
	    nameC="����"
    if numberC==(4):
	    nameC="����"
    return nameC


def rpsls(numberC):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    numberU=name_to_number(nameU)
    nameC=number_to_name(numberC)
    
    
    
    
    if (numberU==0 and numberC==3) or (numberU==0 and numberC==4):
	    print("��Ӯ��")
    elif (numberU==1 and numberC==0) or (numberU==1 and numberC==4):
	    print("��Ӯ��")
    elif (numberU==2 and numberC==1) or (numberU==2 and numberC==0):
	    print("��Ӯ��")
    elif (numberU==3 and numberC==2) or (numberU==3 and numberC==1):
	    print("��Ӯ��")
    elif (numberU==4 and numberC==3) or (numberU==4 and numberC==2):
	    print("��Ӯ��")
    elif numberU==numberC:
        print("ƽ��")
    else:
        print("����Ӯ��")
   

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

# if nameU!="ʯͷ" or nameU!="ʷ����" or nameU!="��" or nameU!="����" or nameU!="����"

# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
nameU=input()
print("----------------")
nameC=number_to_name(numberC)
if nameU in ["ʯͷ","����","��","����","ʷ����"]:
    rpsls(numberC)
    print("����ѡ��Ϊ:%s"%nameU)
    print("�������ѡ��Ϊ:%s"%nameC)
else:
    print("Error:No Correct Name")
