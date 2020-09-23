import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Mailtrap configuration:
username = 'secret'
password = 'secret'

def sendmail(text='Email body', subject='Hello world', from_email='Test email <testmail@mail.com>', to_emails=None, html=None):
    #Throw an error if to_emails is not a list
    assert isinstance(to_emails, list)

    #Create and configure enclosing message
    msg = MIMEMultipart('alternative')
    msg['From'] = 'testmail@mail.com'
    msg['To'] = ', '.join(to_emails) # Separate all email addresses with comma
    msg['Subject'] = subject

    #Create a plain text
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    #Create HTML text
    if html != None:
        html_part = MIMEText('<h1>Hello, this is a test message</h1>', 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    #Login to smtp server
    server = smtplib.SMTP(host='smtp.mailtrap.io', port=2525)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    #Quit process
    server.quit()



