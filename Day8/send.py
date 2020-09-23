#Import module
from formatting import format_msg
import requests
import sys

#Use module
def send(name, website=None, verbose=False):
    #Using imported local module
    if website != None:
        message = format_msg(name=name, website=website)
    else:
        message = format_msg(name=name)
    if verbose:
        print(name, website)

    #Using imported external module
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return 'There was an error'

#Automatically run send() function from console and read arguments that are being sent
if __name__ == '__main__':
    print(sys.argv)
    name = 'Unknown'
    #Read arguments sent from console
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, verbose=True)
    print(response)
