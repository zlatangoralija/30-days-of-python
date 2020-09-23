import os

#Get the current dir of the file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#Set the files dir where we want to send files
files_dir = os.path.join(BASE_DIR, 'images')

#Create a directory if it doesnt exist
os.makedirs(files_dir, exist_ok=True)

#Generate fake images and loop through them
images = range(0, 12)
for i in images:
    #Set image name
    fname = f"{i}.jpg"
    file_path = os.path.join(files_dir, fname)
    #Check if image with given name already exists
    if os.path.exists(file_path):
        print(f"Image {fname} already exists")
        continue
    #Write to every image
    with open(file_path, 'w') as f:
        f.write('Hello world')
