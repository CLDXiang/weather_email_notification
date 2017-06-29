# -*- coding:utf-8 -*-

from Poster import poster
from time import sleep
from datetime import datetime


def main(test=False):
    print('<--天气提醒推送程序启动-->')
    print('版本号v0.2.0')
    with open('./email_list.txt', 'r') as f:
        to_ads = f.read().split('\n')  # 收件人列表（字符串形式）
    # 构造收件人列表（dict形式）
    to_list = []
    for to_ad in to_ads:
        pairs = to_ad.split(',')
        to_a = {}
        for pair in pairs:
            key, value = pair.split(':')
            to_a[key.strip()] = value.strip()
        to_list.append(to_a)

    # 测试
    if test:
        print(datetime.now(), '测试开始...')
        poster.send(to_list)

    flag = False
    while True:
        if 0 < datetime.now().hour < 6 and flag:
            flag = False
            print(datetime.now(), '当日提醒状态重置')
        elif datetime.now().hour == 18 and not flag:
            flag = True
            print(datetime.now(), '当日提醒检查开始...')
            poster.send(to_list)
        sleep(3600)


if __name__ == '__main__':
    main(test=True)
