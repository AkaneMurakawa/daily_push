# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
fish job

:author: AkaneMurakwa
:date: 2021-12-31
"""

from base import send_ding_talk
import random


"""
                            _ooOoo_  
                           o8888888o  
                           88" . "88  
                           (| -_- |)  
                            O\ = /O  
                        ____/`---'\____  
                      .   ' \\| | `.  
                       / \\||| : ||| \  
                     / _||||| -:- |||||- \  
                       | | \\\ - / | |  
                     | \_| ''\---/'' | |  
                      \ .-\__ `-` ___/-. /  
                   ___`. .' /--.--\ `. . __  
                ."" '< `.___\_<|>_/___.' >'"".  
               | | : `- \`.;`\ _ /`;.`/ - ` : | |  
                 \ \ `-. \_ __\ /__ _/ .-` / /  
         ======`-.____`-.___\_____/___.-`____.-'======  
                            `=---='  
  
         .............................................  
                  佛祖保佑             永无BUG 
          佛曰:  
                  写字楼里写字间，写字间里程序员；  
                  程序人员写程序，又拿程序换酒钱。  
                  酒醒只在网上坐，酒醉还来网下眠；  
                  酒醉酒醒日复日，网上网下年复年。  
                  但愿老死电脑间，不愿鞠躬老板前；  
                  奔驰宝马贵者趣，公交自行程序员。  
                  别人笑我忒疯癫，我笑自己命太贱；  
                  不见满街漂亮妹，哪个归得程序员？

"""
FISH_CONFIG = [
    # 0
    '怎么不聊了？忏悔了？又要努力给资本家吸血了？贱不贱啊？什么时候能站起来啊？都把手机掏出来！扔老板脸上！聊他妈的！做新时代的主人！做领导的爹！ '
    '我觉得有些群员心态还是没有放稳，现在这么好的带薪聊天机会，不珍惜，你给老板打工搬砖，你能学到东西吗？你在群里聊天，你培养的交际能力，'
    '是实打实的呀，是跟着你一辈子的呀，不要把眼光老是放在工资工资上面，你将来能力有了，你去哪儿不能高就？说了这么多，一起摸鱼吧。 怎么回事，'
    '好久没人讲话了，今天是工作日啊，工作日不在群里讲话是想干什么，给资本家当走狗吗？我工作日一看到群里的消息断了，我的心就发痛。',
    # 1
    '年终总结：你这一年总共写了60384行代码，总共出现了1887个bug，也就是说你平均32行代码就有一个Bug,你一个人养活了咱们公司一半的测试，你真行，'
    '你这一年总共加班了1824个小时，总共76天，超过了92.3%的同事，还得继续努力啊。你最常用的是ctrl+c, ctrl+v的组合键，光4月30日你就用了212次。'
    '你经常在晚上debug，最晚的一次是凌晨4点，你才把bug清空，技术不太行哦。产品一年给你提了382个需求，你说的最多的一句话是，这个需求我做不了，'
    '一共说了315次，其他常说的是：在我电脑上是正常的，你请下缓存试试。希望你新的一年再接再厉！',
    # 2
    '老板：下班前代码一定要发到线上哈！\n\n'
    '程序员：好的。\n\n'
    '第二天老板到公司了，问：“代码怎么还没有发布到线上啊？昨天不是说下班前吗？”\n\n'
    '程序员：“是的，没错，是下班前，可是我还没下班呢”',
    # 3
    '一个程序员去公司面试，与面试官这样一段对话\n\n'
    '面试官：“你不是16年毕业参加工作的，现在18年了应该是2年工作经验呀，怎么是3年工作经验？那一年从哪来的？”\n\n'
    '程序员：“上家公司一直加班，那一年时间都是加班加出来的！”\n\n'
    '面试官：“。。。。。”\n\n',
    # 4
    '一包茶，一包烟，一个bug改一天',
    # 5 Q都会Q歪来
    '你♞个彬瑞文，你还绿风局局长，q都会q歪来，c你♞，不鲨彬是什么呀\n\n'
    '![bzzb](http://tiebapic.baidu.com/forum/w%3D580/sign='
    '13d1a91da419ebc4c0787691b227cf79/6c969ed0f703918fca0cabb2463d269758eec41f.jpg)',

]


def do_fish_job():
    i = random.randint(0, len(FISH_CONFIG)-1)
    send_ding_talk('fish日常推送', FISH_CONFIG[i])
