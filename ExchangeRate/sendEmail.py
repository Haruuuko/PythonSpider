#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

date = datetime.date.today().strftime('%Y%m%d')

#画图
ratelist = []

fp = open('/Users/Haruko/Desktop/Python_code/bankRate'+date,'r')
fp.next()
fp.next()
for line in fp:
    line = line.strip('\n')
    ratelist.append(str(line.split('      ')[0]))
fp.close()

plt.plot(ratelist)
plt.savefig(date+'.jpg')


# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="wangqing6993@163.com"    #用户名
mail_pass="LISHIYIzsmmd"   #口令 

sender = 'wangqing6993@163.com'
receivers = ['bloodxhand@126.com']
#receivers = ['542872529@qq.com']


bankFile = open('/Users/Haruko/Desktop/Python_code/bankRate'+date).read()
message = MIMEMultipart()
message['From'] = 'haruko<wangqing6993@163.com>'
message['To'] =  'bloodxhand@126.com'
#message['To'] =  '542872529@qq.com'

subject = '今日欧元汇率---来自爱你的python小助手'
message['Subject'] = Header(subject, 'utf-8')

messageText = MIMEText(bankFile, 'plain', 'utf-8')
message.attach(messageText)

picture = open(date+'.jpg','rb')
msgImage = MIMEImage(picture.read())
picture.close()
msgImage.add_header('Content-ID','<meinv_image>')
message.attach(msgImage)

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"   
except smtplib.SMTPException,e:
    print "Error: unable to send email"
    print str(e)
