import os
import sys
import string
import random
import subprocess
import shutil
import time
## Construct the FFmpeg command
#ffmpeg_cmd = ['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-preset', 'fast', '-crf', '23', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', output_file]
# "C:\Users\Heathcliff\Desktop" "C:\Users\Heathcliff\Downloads" 1 0 0 0 "" 
def get_random_string():
    length = 10
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def startMetadataG(folderPath, destinationPath, choiceAuthor, randomChoice1, randomChoice2, choiceAuthor2, fixedAuthor):
    files = os.listdir(folderPath)
    validFiles = []
    validFileExt = [".avi", ".mp4", ".mov"]
    for file in files:
        for perValidExt in validFileExt:
            if (len(file.split(perValidExt)) > 1):
                validFiles.append(file)
    print(validFiles)

    if (len(validFiles) > 0):
        for file in validFiles:
            meta_data = get_random_string()
            subprocess.run(["exiftool", f"-Title={meta_data}", f"-Author={authorDecision(choiceAuthor, randomChoice1, fixedAuthor)}","-overwrite_original", f"{folderPath+chr(92)+file}"])
            if (file.split('.')[1] == "avi"):
                print(f"WARNING - The file: {file} is an AVI format. High chance that the metadata was not changed.")
            else:
                print(f"Changed the meta data of the {file.split('.')[1]} \n Title: {meta_data}")
            time.sleep(.5)
            shutil.move(f"{folderPath+chr(92)+file}", f"{destinationPath}")
            print(f"The file {file} was moved to {destinationPath}")
    else:
        print(f"There aren't any valid files within the folder: {folderPath}")
def authorDecision(choiceAuthor, randomChoice, fixedAuthor):
    if (choiceAuthor == "1"):
        if (randomChoice == "1"):
            return get_random_string()
        else:
            return generateRandomName()
    else:
        return fixedAuthor    
def generateRandomName():
    with open('first-names.txt', 'r') as f:
        my_list = f.readlines()
    finalFirstName = []
    for item in my_list:
        finalFirstName.append(item.split('\n')[0])
    finalLastName = []
    with open('last-names.txt', 'r') as f:
        my_list = f.readlines()
    for item in my_list:
        finalLastName.append(item.split('\n')[0])

    return (random.choice(finalFirstName) + " " + random.choice(finalLastName))            
startMetadataG(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
