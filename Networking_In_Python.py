 #Mailing Client
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
server=smtplib.SMTP('smtp.gmail.com',25)
server.ehlo()
with open('password.txt','r') as f:
    password=f.read()
server.login('ashutosh.pandeyhlr007@gmail.com',password)
msg=MIMEMultipart()
msg['From']='ashutosh.pandeyhlr007@gmail.com'
msg['To']='johncenahlr002@gmail.com'
msg['Subject']='Automating Mails'
with open('Mail.txt','r') as f:
    MailText=f.read()
msg.attach(MIMEText(MailText,'plain'))
filename='27.jpg'
attachment=open(filename,'rb')
payload=MIMEBase('application','octet_stream')
payload.set_payload(attachment.read())
encoders.encode_base64(payload)
payload.add_header('Content-disposition',f'attachment;f{filename}')
msg.attach(payload)
text=msg.as_string()
server.sendmail('ashutosh.pandeyhlr007@gmail.com','johncenahlr002@gmail.com',text)