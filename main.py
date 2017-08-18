# -*- coding:utf-8 -*-

from Poster import poster
from time import sleep
from datetime import datetime
import json


def main(test=False):
    print('<--天气提醒推送程序启动-->')
    print('版本号v0.3.1')
    with open('./config.json', 'r') as f:
        to_list = json.load(f)['emailList']  # [{"email":"","city":""},{"email":"","city":""},{"email":"","city":""}]

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
