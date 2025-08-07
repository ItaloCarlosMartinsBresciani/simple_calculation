import os
import shutil


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")



def create_folders():
    if os.path.exists("Audio") == False:
        os.mkdir("Audio")
    if os.path.exists("Video") == False:
        os.mkdir("Video")
    if os.path.exists("Images") == False:
        os.mkdir("Images")

def organize():
    for file in os.listdir():
        if os.path.splitext(file)[1] in audio:
            shutil.move(file, "Audio")
        elif os.path.splitext(file)[1] in video:
            shutil.move(file, "Video")
        elif os.path.splitext(file)[1] in img:
            shutil.move(file, "Images")

path = input("Enter the path of the folder: ")
os.chdir(path)
create_folders()
organize()
