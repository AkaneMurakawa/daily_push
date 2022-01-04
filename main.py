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
import sys
from weibo_job import do_weibo_job
from fish_job import do_fish_job
from weather_job import do_weather_job


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
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        schedule.every(10).seconds.do(run_threaded, do_weibo_job)
        schedule.every(5).seconds.do(run_threaded, do_fish_job)
        schedule.every(5).seconds.do(run_threaded, do_weather_job)
        while True:
            schedule.run_pending()
        return

    # https://pypi.org/project/schedule/
    # https://schedule.readthedocs.io/en/stable/examples.html
    # weibo_job: 每一小时执行
    schedule.every(ONE_HOUR_IN_SECONDS).seconds.do(run_threaded, do_weibo_job)
    # fish_job: 00, 30分执行
    schedule.every().minutes.at(':00').do(run_threaded, do_fish_job)
    schedule.every().minutes.at(':30').do(run_threaded, do_fish_job)
    # weather_job: 每天九点执行
    schedule.every().day.at("09:00").do(run_threaded, do_weather_job)
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
