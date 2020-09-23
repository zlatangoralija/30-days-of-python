import os

#Get absolute path of file
current_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(current_file_path)
ROOT_PROJECT_DIR = os.path.dirname(BASE_DIR)
#Join BASE_DIR with folder and filename
email_text = os.path.join(BASE_DIR, 'templates', 'email.txt')

content = ''
with open(email_text, 'r') as f:
    content = f.read()
    print(content.format(name='Zlatan'))

