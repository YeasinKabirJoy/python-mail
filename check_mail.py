import os
import imapclient
import imapclient.exceptions
import pyzmail
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


def check_last_email():
    message_status = {
        "success": False,
        "subject":"",
        "body":None,
        "error": ""
    }
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    try:
        imap_obj.login(os.environ['SENDER_MAIL'], os.environ['SENDER_PASSWORD'])
        imap_obj.select_folder('INBOX', readonly=True)
        UIDs = imap_obj.search(['ALL'])
        rawMessages = imap_obj.fetch([UIDs[-1]], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessages[UIDs[-1]][b'BODY[]'])
        message_status["success"] = True
        message_status["subject"] = message.get_subject()
        if message.text_part is not None:
            message_status["body"]=message.text_part.get_payload().decode(message.text_part.charset)
    except imapclient.exceptions.LoginError as e:
        message_status["error"]=e.args[0][2:len(e.args[0])-1]
    finally:
        imap_obj.logout()
    return message_status





# print(message.get_addresses('from'))
# print(message.get_addresses('to'))

# print(message.get_addresses('cc'))
#
# print(message.get_addresses('bcc'))



# print(message.html_part is not None)
#
# print(message.html_part.get_payload().decode(message.html_part.charset))