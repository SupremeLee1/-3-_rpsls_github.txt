#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：
日期：
"""

import random
numberC=random.randint(0,4)#利用randint方法产生0-5之间的随机整数

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(nameU):
    """
    将游戏对象对应到不同的整数
    """

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果
    if nameU=="石头":
	    numberU=int(0)
    if nameU=="史波克":
	    numberU=int(1)
    if nameU=="布":
	    numberU=int(2)
    if nameU=="蜥蜴":
	    numberU=int(3)
    if nameU=="剪刀":
	    numberU=int(4)
    return numberU


def number_to_name(numberC):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果
    
    if numberC==int(0):
	    nameC="石头"
    if numberC==int(1):
	    nameC="史波克"
    if numberC==(2):
	    nameC="布"
    if numberC==(3):
	    nameC="蜥蜴"
    if numberC==(4):
	    nameC="剪刀"
    return nameC


def rpsls(numberC):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    numberU=name_to_number(nameU)
    nameC=number_to_name(numberC)
    
    
    
    
    if (numberU==0 and numberC==3) or (numberU==0 and numberC==4):
	    print("你赢了")
    elif (numberU==1 and numberC==0) or (numberU==1 and numberC==4):
	    print("你赢了")
    elif (numberU==2 and numberC==1) or (numberU==2 and numberC==0):
	    print("你赢了")
    elif (numberU==3 and numberC==2) or (numberU==3 and numberC==1):
	    print("你赢了")
    elif (numberU==4 and numberC==3) or (numberU==4 and numberC==2):
	    print("你赢了")
    elif numberU==numberC:
        print("平局")
    else:
        print("机器赢了")
   

    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

# if nameU!="石头" or nameU!="史波克" or nameU!="布" or nameU!="蜥蜴" or nameU!="剪刀"

# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
nameU=input()
print("----------------")
nameC=number_to_name(numberC)
if nameU in ["石头","剪刀","布","蜥蜴","史波克"]:
    rpsls(numberC)
    print("您的选择为:%s"%nameU)
    print("计算机的选择为:%s"%nameC)
else:
    print("Error:No Correct Name")
