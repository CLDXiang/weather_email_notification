# -*- coding:utf-8 -*-
# 发送邮件


from email.mime.text import MIMEText
from Messenger import messenger
import smtplib
import json

class Poster():
    def __init__(self):
        pass

    def get_text(self, city):
        weather_list = messenger.get_wea(city=city)
        if messenger.whether_notice(wea_list=weather_list):
            # 有糟糕的天气
            print(city + '有糟糕的天气，需要提醒')
            e_text = '今天或明天有糟糕的天气哦！\n' + '这是' + city + '接下来三天的天气：\n'
            for i in range(3):
                e_text += '{:<12}{:<12}{:<5}\n'.format(weather_list[i][0],
                                                       weather_list[i][1],
                                                       weather_list[i][2])
            e_text += '做好准备噢~'
            return e_text
        else:
            # 没有糟糕的天气
            print(city + '天气不错，不用提醒')
            return False

    def get_city_text(self, to_list):
        city_list = list(set([to['city'] for to in to_list if to['city']]))
        text_dict = {}
        for city in city_list:
            text_dict[city] = self.get_text(city)
        return text_dict

    def send(self, to_list):
        with open('./config.json', 'r') as f:
            from_email = json.load(f)['fromEmail']
            from_addr,password = from_email['email'],from_email['password']

        # 输入SMTP服务器地址:
        smtp_server = 'smtp.qq.com'

        server = smtplib.SMTP_SSL(smtp_server)
        # server.set_debuglevel(1)
        server.login(from_addr, password)
        text_dict = self.get_city_text(to_list)
        for to in to_list:
            addr, city = to["email"], to["city"]
            print('\n正在处理 ' + addr)
            text = text_dict[city]
            if text:
                print('正在发送邮件给 ' + addr)
                msg = MIMEText(text, 'plain', 'utf-8')
                msg['From'] = '天气提醒服务器'
                msg['Subject'] = '天气提醒'
                msg['To'] = addr
                server.sendmail(from_addr, [addr], msg.as_string())
                print('邮件发送完成.邮件内容：\n' + text)
        server.quit()


poster = Poster()

if __name__ == '__main__':
    poster.send()
