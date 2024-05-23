# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
weather job

:author: AkaneMurakwa
:date: 2021-12-31
"""

from base import *


def do_weather_job():
    try:
        send_weather()
    except Exception as e:
        log('天气日常推送异常', e, level=LEVEL_ERROR)


def send_weather():
    city = 'Shenzhen'
    language = "zh-CN"
    unit = 'm'

    headers = {
        'Accept-Language': language,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.88 Safari/537.36"',

    }
    url = 'http://wttr.in/' + city + '?format=4&' + unit
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    text = '#### 又是新的一天\n\n'
    text += response.text
    send_ding_talk('天气小助手日常推送', text)


if __name__ == '__main__':
    send_weather()