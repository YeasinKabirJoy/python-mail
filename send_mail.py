import os
import smtplib
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


def send_email(receiver_mail,message):
    message_status = {
        "success":False,
        "error":""
    }
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(os.environ['SENDER_MAIL'], os.environ['SENDER_PASSWORD'])
    try:
        smtp_obj.sendmail(os.environ['SENDER_MAIL'], receiver_mail,
                          f'Subject: {message["subject"]}.\n{message["body"]}')
        message_status["success"] = True
    # except smtplib.SMTPRecipientsRefused as e:
    #     error_message = e.recipients
    #     print(error_message)
    #     print("Mail Sending Failed")
    except smtplib.SMTPSenderRefused as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
        error = f"Error: {error_message.decode('ASCII')} Code: {error_code}"
        message_status["error"] =error
    finally:
        smtp_obj.quit()
    return message_status

