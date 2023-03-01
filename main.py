from send_mail import send_email
from check_mail import check_last_email

if __name__ == '__main__':

    message = {
        "subject": "Testing",
        "body": '''Testing
        multiline'''
    }
    print("--------------Sending mail-----------------------")
    status = send_email("yeasinjoy07@gmail.com", message)
    if status["success"]:
        print("Mail Send")
    else:
        print(status["error"])

    print("----------Checking the last email-----------------")
    status = check_last_email()
    if status["success"]:
        print(f'Subject: {status["subject"]}')
        if status["body"] is not None:
            print(status["body"])
    else:
        print(f'Error:{status["error"]}')