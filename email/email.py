import smtplib
import email.mime.multipart
import email.mime.text

msg=email.mime.multipart.MIMEMultipart()
msg['from']='sm521426@126.com'
msg['to']='13951248462@139.com'
msg['subject']='test'
content='''
   你好，
         这是一封自动发送的邮件。


'''
txt=email.mime.text.MIMEText(content)
msg.attach(txt)

smtp=smtplib.SMTP()
smtp.connect('smtp.126.com','25')
smtp.login('sm521426@126.com','lss0206')
smtp.sendmail('sm521426@126.com','13951248462@139.com',str(msg))
smtp.quit()