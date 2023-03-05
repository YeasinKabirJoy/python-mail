import os
import imaplib
import imapclient #IMAPClient actually uses the imaplib module from the Python standard library under the hood
import pyzmail
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
imaplib._MAXLINE = 10000000


def check_email():
    success = False
    messages = []
    error = ""
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    try:
        imap_obj.login(os.environ['SENDER_MAIL'], os.environ['SENDER_PASSWORD'])
        imap_obj.select_folder('INBOX', readonly=True)
        UIDs = imap_obj.search(['ALL'])
        raw_messages = imap_obj.fetch(UIDs, ['BODY[]', 'FLAGS'])
        for id in UIDs:
            single_message = pyzmail.PyzMessage.factory(raw_messages[id][b'BODY[]'])
            message = {
                "sender": single_message.get_addresses('from'),
                "subject": single_message.get_subject(),
                "body": single_message.text_part.get_payload().decode(single_message.text_part.charset) if single_message.text_part is not None else ""
            }
            messages.append(message)
            success = True
    except imapclient.exceptions.LoginError as e:
        error = e.args[0][2:len(e.args[0]) - 1]
    except imapclient.exceptions.InvalidCriteriaError:
        error = "Invalid Search Arguments"
    finally:
        imap_obj.logout()
    return success,messages,error





# print(message.get_addresses('from'))
# print(message.get_addresses('to'))

# print(message.get_addresses('cc'))
#
# print(message.get_addresses('bcc'))



# print(message.html_part is not None)
#
# print(message.html_part.get_payload().decode(message.html_part.charset))