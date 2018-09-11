# coding=utf-8
import random
#定义获胜次数 获胜三次才能离开
win_times=0
while win_times <= 2 :
    player = input('请输入：剪刀（0） 石头（1） 布（2）')
    player = int(player) #格式转换
    computer = random.randint(0,2)

    #开始逻辑判断
    if((player==0)and(computer==2) or(player==1)and(computer==0)or(player==2)and(computer==1)):
        win_times+=1
        print('哈哈，获胜了，目前您赢了',win_times,'局，请继续努力')
    elif player==computer:
        print('平局，再来一局')
    else:
        print('输了，不要走，洗洗手，决战到天亮！')