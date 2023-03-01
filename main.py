from send_mail import send_email
from check_mail import check_email

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

    print("----------Checking Inbox-----------------")
    success,messages,error = check_email()
    if success:
        print("-------------------------------")
        for single_message in messages[::-1]:
            print(f'From: {single_message["subject"]}')
            print(f'Subject: {single_message["subject"]}')
            print(single_message["body"])
            print("-------------------------------")
    else:
        print(f'Error:{error}')