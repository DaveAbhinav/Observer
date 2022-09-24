import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\shwet\Downloads"
to_dir = "C:\Users\shwet\OneDrive\Desktop\Downloaded files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


#event handler class
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(event)
    


#initialise the event handler class
event_handler=FileMovementHandler()

#Initialise observer
observer=Observer()

#Scheduel the observer
observer.schedule(event_handler,from_dir,recursive=True)

#start the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()


