# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
weibo job

:author: AkaneMurakwa
:date: 2021-12-31
"""

from base import *


def do_weibo_job():
    try:
        for key, value in CONFIG.get('WEIBO_UUID_LIST').items():
            weibo(key, value)
    except Exception as e:
        log('微博日常推送异常', e, level=LEVEL_ERROR)


def weibo(name, uuid):
    """
    根据uuid抓取微博内容
    :param name:
    :param uuid:
    :return:
    """
    page = 1
    query_str = 'uid=' + uuid + '&page=' + str(page) + '&feature=0'
    url = 'https://weibo.com/ajax/statuses/mymblog?' + query_str
    headers = {
        # ':authority': 'weibo.com',
        # ':method': 'GET',
        # ':path': '/ajax/statuses/mymblog?' + query_str,
        # ':scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'SUB=_2AkMWkSsjf8NxqwJRmPEUyGPnbIhxwgzEieKgzdr4JRMxHRl-yT9jqkYNtRB6PREFzHgdAa9t2s1Abq7rtf0sqNEYlTye; '
                  'SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWzBf8v-fSnj81Z75iVDYg2; XSRF-TOKEN=3Na0ASf7-cXGkS-Z-mWyBkrM; '
                  'WBPSESS=IawIaCISeX-46VmeRocrJxM4pvSGijj-vsRdGrGveC0Dwd8Ex-HvNlc9hQDYoH3QLPJZxKotrGB3LA_s1xwTx4tYGYF0'
                  'i84OCnDhA8QAaFZvl-WsZgJ_PmLnzlLijz0pfHiNNHvbCQpP1CoGfebnuHi4xIbYVTlcs5IFLwZ59ZY=',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.159 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json().get('data')
    data_list = data.get('list')

    # 处理微博内容
    process_weibo_to_ding_talk(name, data_list)
    process_weibo_to_markdown(name, data_list)


def process_weibo_to_ding_talk(name, data_list):
    for content in data_list:
        send_weibo_to_ding_talk(name, content)


def process_weibo_to_markdown(name, data_list):
    now_time = time.strftime("%Y%m%d", time.localtime())
    # 文件名称格式：weibo_yyyymmdd.md 例如: weibo_20211231.md
    filename = CONFIG.get('HEXO_PATH') + 'weibo_' + str(now_time) + ".md"
    # 追加
    with open(filename, "a+", encoding='utf-8') as f:
        for content in data_list:
            save_weibo_by_markdown(f, filename, name, content)


def send_weibo_to_ding_talk(name, content):
    """
    发送微博内容到钉钉
    :param name:
    :param content:
    :return:
    """
    # 1
    is_top = content.get('isTop')
    # 微博内容, text_raw, text
    weibo_text = content.get('text_raw')
    # 发布时间, 格式：'Mon Dec 27 12:00:02 +0800 2021'
    created_at = content.get('created_at')
    timestamp = time.mktime(time.strptime(created_at, '%a %b %d %H:%M:%S +0800 %Y'))
    now = time.time()
    # 来源
    source = content.get('source')
    # 图片
    pic_infos = content.get('pic_infos')

    log('微博资源:', content)
    log('微博内容:', weibo_text)
    if is_top and 1 == is_top:
        log('置顶微博, 跳过')
        return
    if now - timestamp > ONE_HOUR_IN_SECONDS:
        log('前1小时后内容, 跳过')
        return

    ding_talk_weibo_text = '#### 【' + name + '的微博】\n\n' + created_at + '来自' + source + '\n\n\n\n'
    ding_talk_weibo_text += weibo_text + '\n\n'

    if pic_infos:
        for pic_key, pic_value in pic_infos.items():
            # 图片大小可选值：thumbnail、bmiddle、large、original、largest、mw2000
            pic = pic_value.get('original').get('url')
            ding_talk_weibo_text += '![screenshot](' + pic + ')'

    ding_talk_title = name + '微博日常推送'
    send_ding_talk(ding_talk_title, ding_talk_weibo_text)
    log(name, '微博日常推送成功', level=LEVEL_WARMING)


def save_weibo_by_markdown(f, filename, name, content):
    """
    保存微博的内容为hexo格式的markdown文件
    :param f: 文件
    :param filename: 文件名称
    :param name: 博主名称
    :param content: 微博内容
    :return:
    """
    # 1
    is_top = content.get('isTop')
    # 微博内容, text_raw, text
    weibo_text = content.get('text_raw')
    # 发布时间, 格式：'Mon Dec 27 12:00:02 +0800 2021'
    created_at = content.get('created_at')
    # 发布时间转换为时间戳
    timestamp = time.mktime(time.strptime(created_at, '%a %b %d %H:%M:%S +0800 %Y'))
    # 当前时间
    now = time.time()
    now_time = time.strftime("%Y%m%d", time.localtime())
    # hexo 文件内容
    hexo_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    hexo_title = '微博日常推送' + str(now_time)
    # 来源
    source = content.get('source')
    # 图片
    pic_infos = content.get('pic_infos')

    log('微博资源:', content)
    log('微博内容:', weibo_text)
    if is_top and 1 == is_top:
        log('置顶微博, 跳过')
        return
    if now - timestamp > ONE_HOUR_IN_SECONDS:
        log('前1小时后内容, 跳过')
        return

    # 写入内容
    weibo_file_text = '### ' + name + '的微博\n' + created_at + '来自' + source + '\n<br/>'
    weibo_file_text += weibo_text

    if pic_infos:
        for pic_key, pic_value in pic_infos.items():
            # 图片大小可选值：thumbnail、bmiddle、large、original、largest、mw2000
            pic = pic_value.get('original').get('url')
            # 设置显示的图片大小
            weibo_file_text += '<img width="360" src="' + pic + '"/>\n'
    # 每条微博写入间隔处理
    weibo_file_text += '\n<br/><br/>\n'
    # 初次写入
    if 0 == os.path.getsize(filename):
        # 写入hexo的markdown格式
        hexo = '---\n' + \
               'title: ' + hexo_title + '\n' + \
               'date: ' + hexo_date + '\n' + \
               '---\n'
        f.write(hexo)
    f.write(weibo_file_text)
    log(name, '微博日常写入成功', level=LEVEL_WARMING)
