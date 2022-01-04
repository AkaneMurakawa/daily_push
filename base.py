# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
base模块

:author: AkaneMurakwa
:date: 2021-12-31
"""

import requests
import json
import time
import os

"""=================================================基础数据==========================================================="""
# JOB
ONE_HOUR_IN_SECONDS = 1 * 60 * 60

# 日志
LEVEL_INFO = 0
LEVEL_ERROR = 1
LEVEL_WARMING = 2
LEVEL_DEBUG = 3
LOG_LEVEL = {
    LEVEL_INFO: 'INFO',
    LEVEL_ERROR: 'ERROR',
    LEVEL_WARMING: 'WARMING',
    LEVEL_DEBUG: 'DEBUG'
}

"""=================================================配置信息==========================================================="""
CONFIG = {
    # 钉钉
    'DING_TALK_URL': 'https://oapi.dingtalk.com/robot/send?access_token='
                     'af6a8a0698e2ede31a380d69d3df4b3f8d6a4d405b6e966501445a28d5504cfc',
    # 微博UUID, key: 博主名(自定义)， value: uuid
    'WEIBO_UUID_LIST': {
        'GitHubDaily': '5722964389',
        'HelloGitHub': '5692692520',
        '算法时空': '5819320755',
        'Easy': '1088413295',
    },
    # 日志等级
    'LOG_LEVEL': LEVEL_WARMING,
    # 日志文件大小限制，单位:字节，默认1MB
    'LOG_LIMIT_SIZE_BYTE': 1 * 1024 * 1024,
    # hexo资源路径，以/尾巴
    'HEXO_PATH': '/data/data/com.termux/files/home/blog/source/_posts/',
}

"""=================================================公共组件==========================================================="""


def log(*args, level=LEVEL_DEBUG, sep='', end='\n'):
    """
    日志记录
    :param sep: 多个参数直接分割符
    :param args: 参数
    :param level: 日志等级
    :param end: 结尾处理
    :return:
    """
    if level > CONFIG.get('LOG_LEVEL'):
        return

    filename = 'log.' + LOG_LEVEL.get(int(level)).lower()
    with open(filename,  "a+", encoding='utf-8') as f:
        # 超过文件上线大小则清空
        if os.path.getsize(filename) > CONFIG.get('LOG_LIMIT_SIZE_BYTE'):
            f.seek(0)
            f.truncate()

        print('[' + LOG_LEVEL.get(int(level)) + ']', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '>>',
              end='', file=f)
        print(*args, sep=sep, end=end, file=f)


# noinspection PyBroadException
def send_ding_talk(title, text):
    """
    发送钉钉通知，如果你需要@某人，那么你需要设置atMobiles
    文档：https://open.dingtalk.com/document/group/custom-robot-access
    注意：钉钉消息markdown格式换行是双\n：\n\n
    :param text:
    :param title:
    :return:
    """
    headers = {
        'Accept-Encoding': '',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }
    data = {
        'msgtype': 'markdown',
        'markdown': {
            'title': title,
            'text': text
        },
        'at': {
            'isAtAll': False
        }
    }
    try:
        response = requests.post(CONFIG.get('DING_TALK_URL'), headers=headers, data=json.dumps(data))
        response.raise_for_status()
    except Exception as e:
        log('钉钉推送失败', e, level=LEVEL_ERROR)
    # 防止发送的频率过高
    time.sleep(2)

