import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os



def send_email(body):
    host = "smtp.gmail.com"
    port = 465
    username = "jeremyabraham17@gmail.com"
    password = os.getenv("DailyNewsApp")
    receiver = "jeremyabraham17@gmail.com"
    context = ssl.create_default_context()
    
    
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = "Daily News Update"
    
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())



