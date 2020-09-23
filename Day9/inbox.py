import imaplib
import email

#Mailtrap configuration
host = 'smtp.mailtrap.io'
username = 'secret'
password = 'secret'

def get_inbox():
    #Login to mailtrap and select the inbox that we want to read
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select('inbox')

    #Get unread mails
    # "_" represents placeholder variable, that will not be used
    _, search_data = mail.search(None, 'UNSEEN')

    messages = []

    #Loop through all the unread emails
    #Use the split method here, since the data is formatted like (b '4 5 6'), to create a list: [b'4, b'5, b'6]
    for num in search_data[0].split():
        email_data = {}

        #Fetch the mail with given number
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        #Get the message from bytes as string
        email_message = email.message_from_bytes(b)

        # Get the message headers
        for header in ['subject', 'to', 'from', 'date']:
            print('{}: {}'.format(header, email_message[header]))
            email_data['header'] = email_message[header]

        #Parse this email message
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
                print(body.decode())
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
                print(html_body.decode())

            messages.append(email_data)

    return messages

#Call  function from console
if __name__ == '__main___':
    my_inbox = get_inbox()
    print(my_inbox)


