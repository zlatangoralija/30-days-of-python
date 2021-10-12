import requests
import os
import shutil
from download_util import download_file

#Define all the dirs
CURRENT_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(CURRENT_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')

#Create downloads folder if it doesn't exist
os.makedirs(DOWNLOADS_DIR, exist_ok=True)
downloaded_image_path = os.path.join(DOWNLOADS_DIR, 'lake.jpg')

#Get crater lake image from given url
url = 'https://www.laketemperature.org/wp-content/uploads/2019/11/Crater-Lake.jpg'
image = requests.get(url, stream=True)

#Get exception if status != 200
image.raise_for_status()

#First case: Small files
#Open image in binary/write mode
with open(downloaded_image_path, 'wb') as img:
    #Put request content (image) in the downloads dir
    img.write(image.content)

#Second case: Large files

#Call the custom function
download_file(url, DOWNLOADS_DIR)