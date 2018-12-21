#-*- coding:utf-8 -*-
from wxpy import *
import requests
# 初始化机器人，扫码登陆
bot = Bot()



def send_news(str):
    try:

        print(bot.friends().search(u'充电宝宝')[0])
        # 微信昵称，不是账号
        my_friend = bot.friends().search(u'充电宝宝')[0]
        #发送
        my_friend.send(str)
        #发送图片
        #my_friend.send_image("C:\\Users\\Administrator.000\\Desktop\\intiloading.png")
        # 发送视频
        #my_friend.send_video('my_video.mov')
        # 发送文件
        #my_friend.send_file('my_file.zip')
        # 以动态的方式发送图片   没啥用
        # my_friend.send('@img@C:\\Users\\Administrator.000\\Desktop\\intiloading.png')
        # t = Timer(86400,send_news("kaishi"))
        # t.start()

        #bot对象里含有chats，friends，groups，mps等方法，分别可以获取当前机器人的聊天对象、好友、群聊、公众号等信息
        #all_group = bot.groups()
        #print("type all:",type(all_group))
        #print(all_group)  #[<Group: 兑换狂人软件开发内部交流群>, <Group: 自足智能科技，百事通>]
        #for i in all_group:
        #    Group = str(i)
        #    group = Group.replace("<Group: ","").replace(">","")
        #    #send=bot.groups().search(group)[0].send_image("1.jpg")
        #    print(Group)
        #    print(group)
        #    # print(send)

    except :
        my = bot.friends().search(u'帅小浪🌻⁶⁶⁶₆₆₆')[0]
        my.send("发送失败了")

if __name__ == '__main__':
    # str = input("输入q退出")
    # if str == "q":
    #     exit(0)
    # else:

    send_news("我在测试程序")

    #sys.exit()
    embed()
