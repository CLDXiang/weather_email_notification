# -*- coding:utf-8 -*-
# 得到天气信息

import datetime
import requests
import json


class Messenger():
    def __init__(self):
        with open('./config.json', 'r') as f:
            self.KEY = json.load(f)['HEKey']
            self.num2cn = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '日'}

    def get_wea(self, record=False, city='上海'):
        api_url = 'https://free-api.heweather.com/v5/forecast?city={city}&key={key}'.format(city=city, key=self.KEY)
        wea_list = []  # weather

        print('正在从 free-api.heweather.com 获取' + city + '的天气信息...')
        # sleep(3)
        page = requests.get(api_url)
        page.encoding = 'utf-8'
        wea_info = page.json()

        for i, day_info in enumerate(wea_info['HeWeather5'][0]['daily_forecast']):
            date = day_info['date'][-2:] + '日'
            if i == 0:
                date += '(今天)'
            elif i == 1:
                date += '(明天)'
            elif i == 2:
                date += '(周{})'.format(self.num2cn[(datetime.datetime.now() + datetime.timedelta(days=2)).isoweekday()])
            wea_list.append((date, day_info['cond']['txt_d'] + '-' + day_info['cond']['txt_n'],
                             day_info['tmp']['min'] + '/' + day_info['tmp']['max']))

        print('获取' + city + '天气信息完成')

        if record:
            with open('./record.txt', 'w') as f:
                for day in wea_list:
                    f.write(' '.join(day) + '\n')
            print('已将记录写入record.txt')

        return wea_list

    def whether_notice(self, wea_list, day=2):
        '''
        :param wea_list: [(day,weather,temperature),(day,weather,temperature),...]
        :param day: how many days. default: today and tomorrow.
        :return: True/False
        '''
        for wea in wea_list[:day]:
            if any([(i in wea[1]) for i in ['雨', '雪', '冰', '霾', '暴']]):
                return True
        return False


messenger = Messenger()

if __name__ == '__main__':
    messenger.get_wea(record=True)
