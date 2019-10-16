#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#author:inwell
#Time:2019/10/16 14:45
#购物车小程序
# (1)    要求顾客输入他拥有的钱。
# (2)    展示商品的序号，名称及其价格。
# (3)    输入要买的商品的序号。
# (4)    如果序号输入有误就提示用户重新输入。
# (5)    输入要买的商品的数量。
# (6)    购物车中显示购买的商品名称及其对应的数量和剩余钱。
# (7)    如果钱不够了提示用户钱不够，并且退出程序。

# 思路如下：
# 1、首先创建一个购物车，用来存放顾客购买的东西
# 2、请顾客输入他所拥有的金钱的数量，再判断一下顾客输入的是否为数字
# 3、展示我们的商品的序号，名称和价格
# 4、请顾客输入想要购买的商品的序号
# 5、判断序号是否符合要求，如果有误就提示用户重新输入
# 6、请顾客输入想要购买的商品的数量
# 7、把顾客购买的商品的名称，数量加入购物车，并计算顾客剩余的钱
# 8、如果顾客剩余的钱不够，则提示顾客，并退出程序；否则显示购物车的内容，和顾客剩余的钱

#商品列表
product_list=[
    {'name':'苹果','price':10},
    {'name':'香蕉','price':15},
    {'name':'西瓜','price':12},
    {'name':'草莓','price':30},
    {'name':'桃子','price':20}
]
#购物车
shop_list={}
sum_money=input("请输入您的钱：")
while 1:
    if sum_money.isdigit() and int(sum_money)>0:
        print("--------欢迎来到沃尔玛购物中心---------")
        for k,v in enumerate(product_list):
            print("商品序号：",k,"商品名称：",v['name'],"商品价格：",v['price'])
        print("--------欢迎来到沃尔玛购物中心---------")

        p_number=input("请输入您要购买的商品序号：")
        if p_number.isdigit() and int(p_number)<len(product_list):
            p_count=input("请输入您要购买的商品数量：")
            if p_count.isdigit() and int(p_count):
                # 7、把顾客购买的商品的名称，数量加入购物车，并计算顾客剩余的钱
                #在python3中input输出的都是str
                #把序号转换成int类型，
                p_number=int(p_number)
                p_count=int(p_count)
                shop_list['name']=product_list[p_number]['name']
                shop_list['number']=int(p_count)
                #顾客剩余的钱
                result_money=int(sum_money)-product_list[p_number]['price']*p_count
                print("你还有：",result_money,"块钱！")
                if result_money<=0:
                    print("\033[31;40m 钱不够了，无法购买! \33[0m")
                    break
                else:
                    #显示购物车的内容，和顾客剩余的钱
                    print('购物车中有：',shop_list)
            else:
                print("请输入数字,并且数量至少为1")
        else:
            print('\033[31;40m 商品序号为0-4以内的数字 \33[0m')
    else:
        print("请输入数字,钱必需大于0，否则无法购买商品")





