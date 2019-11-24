#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：
日期：
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果
    if name=="石头":
	    number=0
    if name=="史波克":
	    number=1
    if name=="布":
	    number=2
    if name=="蜥蜴":
	    number=3
    if name=="剪刀":
	    number=4
    elif name!=("石头" or "史波克" or "布" or "蜥蜴" or "剪刀"):
	    number=5
    return number


def number_to_name(number7):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果
    
    if number7==0:
	    name7="石头"
    if number7==1:
	    name7="史波克"
    if number7==2:
	    name7="布"
    if number7==3:
	    name7="蜥蜴"
    if number7==4:
	    name7="剪刀"
    return name7


def rpsls(number7):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    number=name_to_number(name)
    number7=random.randint(0,5)#利用randint方法产生0-5之间的随机整数
    
    
    if number==0 and (number7==3 or 4):
	    print("你赢了")
    elif number==1 and (number7==0 or 4):
	    print("你赢了")
    elif number==2 and (number7==1 or 0):
	    print("你赢了")
    elif number==3 and (number7==2 or 1):
	    print("你赢了")
    elif number==4 and (number7==3 or 2):
	    print("你赢了")
    elif number7==0 and (number==3 or 4):
	    print("机器赢了")
    elif number7==1 and (number==0 or 4):
	    print("机器赢了")
    elif number7==2 and (number==1 or 0):
	    print("机器赢了")
    elif number7==3 and (number==2 or 1):
	    print("机器赢了")
    elif number7==4 and (number==3 or 2):
	    print("机器赢了")
    elif number==5:
	    print("Error: No Correct Name")
   

    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”



# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
name=input()
print("----------------")
number7=number7=random.randint(0,5)#利用randint方法产生0-5之间的随机整数
rpsls(number7)
name7=number_to_name(number7)
print("您的选择为:%s"%name)
print("计算机的选择为:%s"%name7)
