自动获取天气信息并在有雨雪等糟糕天气时发邮件通知。

## 发件邮箱设置
发件邮箱设置位于`"./from_email.txt"`，共两行，分别记录发件邮箱地址和密码。
```angular2html
name@server.com # 发件邮箱地址
password # 发件邮箱密码
```

## 收件人列表构造
收件人列表位于`"./email_list.txt"`中，每行记录一个收件人，以`email:***@***,city:,service:w`dict形式记录。
```angular2html
email:***@***,city:上海,service:w
email:***@***,city:上海,service:w
email:***@***,city:北京,service:w
...
```
可用城市与其对应ID在`"./city_id.txt"`中查询。

## 注意
当前多数邮箱会将此程序发送的邮件放入垃圾箱中，故需要收件人将发件邮箱地址加入白名单中。