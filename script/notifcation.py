import smtplib
from email.mime.text import MIMEText
from email.header import Header

SMTP_SERVER_QQ = "smtp.qq.com"
SMTP_PORT_QQ = 465

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def email_message(from_who, to_who, title, body):
    message = MIMEText(body, 'plain', 'utf-8')

    message['Subject'] = Header(title, 'utf-8')
    message['From'] = Header(from_who, 'utf-8')
    message['To'] = Header(to_who, 'utf-8')

    return message


def notify_by_email(from_email, to_email, password, smtp_server, smtp_port, msg):
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_email, password)
    server.sendmail(from_email, [to_email], msg.as_string())
    server.quit()
