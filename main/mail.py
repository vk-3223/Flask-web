from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg_height):
    from_email = "venilkhunt3223@gmail.com"
    from_password = "Vkhunt233263g"
    to_email = email

    subject = "Height Data"
    message = "Hey there, your height is <strong>%s</strong>.A avrage_height is <strong>%s</strong>" %(height, avg_height)

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)