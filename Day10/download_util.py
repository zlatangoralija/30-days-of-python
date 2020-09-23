import os
import shutil
import requests

def download_file(url, dir, fname=None):
    # Get file name from file itself
    if fname == None:
        file_name = os.path.basename(url)

    # Create a new path for this file
    download_path = os.path.join(dir, file_name)

    # Keep the request open, until the file downloads
    with requests.get(url, stream=True) as request:
        # Move file to downloads folder
        with open(download_path, 'wb') as file:
            shutil.copyfileobj(request.raw, file)

    return download_path
