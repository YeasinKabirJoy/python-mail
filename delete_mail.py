import os
import imapclient
import imapclient.exceptions
import pyzmail
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


def delete_email(UIDs):
    success = False
    error = ""
    deleted_uid = ''
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    try:
        imap_obj.login(os.environ['SENDER_MAIL'], os.environ['SENDER_PASSWORD'])
    except imapclient.exceptions.LoginError as e:
        error = e.args[0][2:len(e.args[0]) - 1]
    try:
        imap_obj.select_folder('INBOX', readonly=False)
        result = imap_obj.delete_messages(UIDs)
        deleted_uid = [uid for uid in result.keys()]
        # imap_obj.expunge() gmail automatically expunge the deleted messages
        success = True
    except imapclient.exceptions.InvalidCriteriaError:
        error = "Invalid Search Arguments"
    finally:
        imap_obj.logout()
    return success,deleted_uid, error
