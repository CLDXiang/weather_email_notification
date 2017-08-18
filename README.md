自动获取天气信息并在有雨雪等糟糕天气时发邮件通知。

## 发件邮箱设置
文件`"./email_config.json"`中的`"fromEmail"`为发件邮箱设置。
```angular2html
{
"email":"", # 发件邮箱地址
"password":"" # 发件邮箱密码
} 
```

## 收件人列表设置
文件`"./email_config.json"`中的`"emailList"`为收件人列表设置，其中每个对象记录一个收件人。
```angular2html
[
{
"email":"", # 收件邮箱地址
"city":"", # 所在城市名（使用city_id中存在的城市名）
"service":"" # 服务（未来的功能）
},
{
"email":"",
"city":"",
"service":""
},
...
]
```
可用城市与其对应ID在`"./city_id.txt"`中查询。

## 注意
当前多数邮箱会将此程序发送的邮件放入垃圾箱中，故需要收件人将发件邮箱地址加入白名单中。