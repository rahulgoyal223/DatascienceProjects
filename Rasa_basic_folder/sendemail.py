import smtplib
from email.message import EmailMessage

from_email = "rahulsumiranchatbot@gmail.com"
password = "Upgrad@123"
subject = "Restaurant Search Result"

def send_email(to_email,message):
    print("Email: {} message: {}".format(to_email,message))
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(from_email,password)
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    server.sendmail(from_email,to_email,msg.as_string())
    server.quit()

#send_email(to_email='rahul.goyal223@live.com',message='test')