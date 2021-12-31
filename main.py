# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
日常推送

:author: AkaneMurakwa
:date: 2021-12-31
"""

from base import *
import schedule
import threading
from weibo_job import do_weibo_job
from fish_job import do_fish_job


def run_threaded(job_func):
    # 创建一个线程执行对应函数
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def before():
    """
    前置处理
    :return:
    """
    log('----------------------------------------------------------', level=LEVEL_INFO)
    log('\t\t\t正在进行日常推送...', level=LEVEL_INFO)
    log('----------------------------------------------------------', level=LEVEL_INFO)


def run():
    """
    执行任务
    :return:
    """
    # weibo_job
    schedule.every(ONE_HOUR_IN_SECONDS).seconds.do(run_threaded, do_weibo_job)
    # fish_job
    schedule.every(HALF_HOUR_IN_MINUTES).minutes.do(run_threaded, do_fish_job)
    while True:
        schedule.run_pending()


def after():
    """"
    后置处理
    """
    pass


if __name__ == '__main__':
    before()
    run()
    after()