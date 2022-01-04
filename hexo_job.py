# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
日常推送

:author: AkaneMurakwa
:date: 2022-1-4
"""

import os
from base import *


def do_hexo_job():
    try:
        os.system('cd ~/blog')
        os.system('hexo generate &')
    except Exception as e:
        log('hexo执行日常推送异常', e, level=LEVEL_ERROR)


