from ComposeEmail import *
from ReadEmail import *
from TalkandListen import *

def Login():
    talk("Login Successful !")
    UserMakesChoice()

def UserMakesChoice():
    talk("Do you wish to read or compose an email ?")
    if get_info() == 'read':
        talk('You Have chosen to Read Emails')
        ReadingTheEMails()
    elif get_info() == 'compose':
        talk('You Have chosen to Compose an Email')
        compose_mail()
    else:
        talk('Wrong Choice')

Login()