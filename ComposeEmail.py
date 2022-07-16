import smtplib
from email.message import EmailMessage
from TalkandListen import *

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # port address of gmail server.
    # sends to gmail server and then sends it to recipent.

    server.starttls()  # initialize the process for sending mail
    server.login('201900449@vupune.ac.in', 'Tejo@10dec')  # gmail credentials
    email = EmailMessage()  # inbuilt function to send an email
    email['From'] = 'alekhyat10@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)  # sender  to receiver via server.

'''email_list = {
    'Mihir': 'mihirthakkar.t@gmail.com',
    'myself': 'alekhyat10@gmail.com',
    'dad': 'prasadtlaa@gmail.com',
    'brother': 'aniruddh832@gmail.com'
}
'''
def receiver_confirmation(confirm):
    if 'yes' not in confirm:
        get_receiver()
    return 0

def subject_confirmation(confirm):
    if 'yes' not in confirm:
        get_subject()
    return 0

def content_confirmation(confirm):
    if 'yes' not in confirm:
        get_content()
    return 0

def get_receiver():
    talk('Hey Alekhya ! To Whom You Want To Send An Email?')
    receiver = get_info()
    #reomve spaces, append '@gmail.com' string
    print(receiver)
    talk("You have said : ")
    talk(receiver)
    talk("Are you sure of this recipient ?")
    if receiver_confirmation(get_info()) == 0:
        get_subject(receiver)

def get_subject(receiver):
    talk('What Is The Subject Of Your Email ?')
    subject = get_info()
    talk("You have said : ")
    talk(subject)
    talk("Are you sure of this subject ?")
    if subject_confirmation(get_info()) == 0:
        get_content(receiver,subject)

def get_content(receiver,subject):
    talk('Tell Me The Text')
    message = get_info()
    talk(message)
    talk('Are You Sure You Want To Send This?')
    if content_confirmation(get_info()) == 0:
        talk("Successfully sent email.")
        send_email(receiver, subject, message)

def compose_mail():
    get_receiver()
    talk('Do You Want To Send More Emails?')
    approve = get_info()

    if 'yes' in approve:
        compose_mail()
    else:
        talk('Thank you for using this')
        exit()

def reply(receiver,subject):
    talk('Tell Me The Text')
    message = get_info()
    talk(message)
    talk('Are You Sure You Want To Send This?')
    if content_confirmation(get_info()) == 0:
        talk("Successfully sent email.")
        send_email(receiver, subject, message)