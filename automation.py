from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import os.path

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            extension = os.path.splitext(filename)[1]
            if extension in image:
                new_destination = folder_dict["images"] + "/" + filename
            elif extension == java:
                new_destination = folder_dict["java"] + "/" + filename
            elif extension == python:
                new_destination = folder_dict["python"] + "/" + filename
            elif extension == zip_extension:
                new_destination = folder_dict["zip"] + "/" + filename
            elif extension == pdf:
                new_destination = folder_dict["pdf"] + "/" + filename
            elif extension in doc:
                new_destination = folder_dict["docx"] + "/" + filename
            else:
                new_destination = folder_dict["other"] + "/" + filename
            
            os.rename(src, new_destination)

folder_to_track = "/Users/krodriguez/Downloads"
folder_dict = {"image": "/Users/krodriguez/Desktop/Images",
                        "zip": "/Users/krodriguez/Desktop/Zip",
                        "pdf": "/Users/krodriguez/Desktop/PDF",
                        "java": "/Users/krodriguez/Desktop/Java",
                        "python": "/Users/krodriguez/Desktop/Python",
                        "docx": "/Users/krodriguez/Desktop/Documents",
                        "other": "/Users/krodriguez/Desktop/Other"}

image = [".png",".jpeg",".jpg",".gif"]
java = ".java"
python = ".py"
zip_extension = ".zip"
pdf = ".pdf"
doc = [".docx",".txt"]
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
