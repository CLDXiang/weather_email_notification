# -*- coding:utf-8 -*-
# 爬取天气信息

import re
import requests
from lxml import etree
from time import sleep


class Crawler():
    def __init__(self):
        self.cities_dict = {}  # 城市dict{city_name:city_id}
        with open('./city_id.txt', 'r') as f:
            cities = f.read().split('\n')
            for city in cities:
                name, ID = city.split(',')
                self.cities_dict[name.strip()] = ID.strip()

    def get_wea(self, record=False, city='上海'):
        weather_url = 'http://www.weather.com.cn/weather/{}.shtml'.format(self.cities_dict[city])
        headers = {'Host': 'www.weather.com.cn',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate, sdch', 'Referer': 'https', 'Accept-Language': 'zh-CN,zh;q=0.8',
                   'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                   'Connection': 'keep-alive'}
        wea_list = []  # weather

        print('正在从 www.weather.com.cn 获取' + city + '的天气信息...')
        sleep(3)
        page = requests.get(weather_url, headers=headers)
        page.encoding = 'utf-8'
        html = etree.HTML(page.content)
        container_list = html.xpath('.//div[@class="c7d"]/ul[@class="t clearfix"]/li[@class]')
        for li in container_list:
            day = li.xpath('./h1/text()')[0].strip()
            weather = li.xpath('./p[@class="wea"]/text()')[0]
            temperature = ''.join(
                '/'.join(re.findall('>\d+', etree.tostring(li.xpath('./p[@class="tem"]')[0]).decode('utf-8'))).split(
                    '>'))
            wea_list.append((day, weather, temperature))
        print('获取' + city + '天气信息完成')

        # with open('page.html','w') as f:
        #     f.write(page.text)

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
            if any([(i in wea[1]) for i in ['雨', '雪', '冰', '霾']]):
                return True
        return False


crawler = Crawler()

if __name__ == '__main__':
    crawler.get_wea(record=True)
