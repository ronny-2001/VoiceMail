import email
import imaplib
from TalkandListen import *

def getMailContent(data):
    raw_email = data[0][1]
    # converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    b = email.message_from_string(raw_email_string)
    body=''
    if b.is_multipart():
        for part in b.walk():

            ctype = part.get_content_type()
            #print("CTYPE : ",ctype)
            cdispo = str(part.get('Content-Disposition'))
            #print("CDISPO : ",cdispo)

            # skip any text/plain (txt) attachments
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)  # decode
            else:
                if part.get('Content-Disposition') is None:
                    continue
                fileName = part.get_filename()
                break
    # not multipart - i.e. plain text, no attachments, keeping fingers crossed
    else:
        body = b.get_payload(decode=True)
    return [body,fileName]

#if we want to download those attachements.

'''if bool(fileName):
            filePath = os.path.join('/Users/sanketdoshi/python/', fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()'''

# If no specific subject or sender than = 'ALL'
# If specific subject then =  '(SUBJECT "The actual subject comes here")'
# If specific sender then =  '(FROM "sender comes here")'
# If both = '(FROM "sender comes here" SUBJECT "The actual subject comes here")'

#example : -
#data = mail.search(None, '(FROM "anjali sinha" SUBJECT "test")' )
#def case 1-

def Read(string1,mail):
    mail.select("inbox")
    status, data = mail.search(None, string1)
    mail_ids = []
    if len(mail_ids)==0:
        talk("No Such emails")
    for block in data:
        mail_ids += block.split()

    for i in mail_ids:
        status, data = mail.fetch(i, '(RFC822)')

        for response_part in data:
            # so if its a tuple...
            if isinstance(response_part, tuple):

                print(response_part[0])
                print(response_part[1])
                message = email.message_from_bytes(response_part[1])

                mail_from = message['from']
                mail_subject = message['subject']
                #mail_to = message['To']
                #mail_toCC = message['Cc']

                content = getMailContent(data)
                mail_content = content[0]
                fileName = content[1]

                #result
                talk(f'From: {mail_from}')
                print("Spoke receiptent")

                """talk(f'From: {mail_to}')
                print("Spoke reciever1")
                talk(f'From: {mail_toCC}')
                print("Spoke reciever2")"""

                talk(f'Subject: {mail_subject}')
                print("Spoke subject")
                talk(f'Content: {mail_content}')
                print("Spoke content")
                talk(f'Files Attached: {fileName}')
                print("Spoke files")


def case1():
    str=" "
    talk("Enter the subject to search for")
    subject = get_info()
    str = '(SUBJECT "'+subject+'")'
    return str

def case2():
    str=" "
    talk("Enter the Receiptent to search for")
    inputFrom = get_info()
    str = '(FROM "'+inputFrom+'")'
    return str

def case3():
    str=" "
    talk("Enter the Receiptent to search for")
    inputFrom = get_info()
    str = '(FROM "' + inputFrom + '" '

    # If both = '(FROM "sender comes here" SUBJECT "The actual subject comes here")'
    talk("Enter the subject to search for")
    subject = get_info()
    str1 = str + 'SUBJECT "' + subject + '")'
    return str1

def Options(instruction,mail):
    if instruction == "subject":
        str=case1()
    elif instruction == "from":
        str=case2()
    elif instruction == "both":
        str=case3()
    elif instruction == "0":
        str="ALL"
    else :
        talk('Invalid input')
        ReadingTheEMails()
    Read(str,mail)
#currently taking user input hardcoded later use listener

def ReadingTheEMails():
    EMAIL = "201900449@vupune.ac.in"
    PASSWORD = "Hopeless@VUSince2019"
    SERVER = 'imap.gmail.com'

    # connect to the server and go to its inbox
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)

    talk(f'Say Subject to read mail using Subject, FROM to read mail using Receiptent , Both to read mail using both Subject and Receiptent or, Say 0 for none')
    instruction = get_info()
    talk("You have said Option ")
    talk(instruction)
    Options(instruction,mail)
