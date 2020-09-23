from formatting import format_msg
import requests
import sys
from sendmail import sendmail

#Use module
def send(name, website=None, verbose=False, to_email=None):
    # Throw an error if to_email is empty
    assert to_email != None

    #Using imported local module
    if website != None:
        message = format_msg(name=name, website=website)
    else:
        message = format_msg(name=name)
    if verbose:
        print(name, website, email)

    #Send message with sendmail module
    try:
        sendmail(text=message, to_emails=[to_email], html=None)
        sent = True
    except:
        sent = False

    return sent

#Automatically run send() function from console and read arguments that are being sent
if __name__ == '__main__':
    print(sys.argv)
    name = 'Unknown'
    email = 'Unknown'

    #Read arguments sent from console
    if len(sys.argv) > 1:
        name = sys.argv[1]
    if len(sys.argv) > 2:
        email = sys.argv[2]

    response = send(name, verbose=True, to_email=email)
    print(response)
