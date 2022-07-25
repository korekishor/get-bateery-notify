"""
import smtplib
# print("--------------------",help(smtplib))
mail_from = 'kishorkore1999@gmail.com'
mail_to = ['k.kore@rnt.ai']
mail_subject = 'Hello'
mail_message_body = 'Hello World!'

mail_to_string = ', '.join(mail_to)

mail_message = f'''
From: {mail_from}
To: {mail_to_string}
Subject: {mail_subject}

{mail_message_body}
'''

server = smtplib.SMTP('localhost')
server.sendmail(mail_from, mail_to, mail_subject, mail_message)
server.quit()"""

"""
import smtplib

sender="kishorkore1999@gmail.com"
receiver="kishorkore1999@gmail.com"

password=input(str("enter your passworld : "))
msg="hey this is kishor have send mail by using python"


server=smtplib.SMTP('smtp.gmail.com',465)
server.starttls()
server.login(sender,password)
print("login succesfully ")

server.sendmail(sender,receiver,msg)

print("mail send succesfully")

"""


"""
import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg['Subject']='Trainig invation'
msg['From']='Mukesh training team'
msg['To']='kishorkore1999@gmail.com'
msg.set_content(" test email from kishor ")

"""



# import smtplib

# conn=smtplib.SMTP('smtp.gmail.com',587)

# conn.ehlo()
# conn.starttls()

# def emailinput():
#     sender_email=input("enter the mail id :")
#     print(sender_email)
#     return sender_email

# emailinput()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You '''

SERVER = "localhost"

#The mail addresses and password
sender_address = 'kishorkore1999@gmail.com'
sender_pass = '7558377276'
receiver_address = 'kishorkore1999@gmail.com'
#Setup the MIME

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail

message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail

session = smtplib.SMTP('smtp.gmail.com') #use gmail with port

session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')



