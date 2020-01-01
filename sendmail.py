#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="syaobinbill@163.com"    #用户名
mail_pass="wy@FMJ28"   #口令


sender = 'syaobinbill@163.com'
receivers = ['alexsun86@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建带附件实例
message = MIMEMultipart()
message['From'] = 'bigcat<syaobinbill@163.com>'
message['To'] = 'littlecat<alexsun86@163.com>'
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 正文内容
message.attach(MIMEText('动物园开张通知', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件  文件名不能出现中文名
# att1 = MIMEText(open('test.caj', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="test.caj"'
# message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
# att2 = MIMEText(open('test1.py', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="test1.py"'
# message.attach(att2)

print("开始发送邮件")

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(e)
