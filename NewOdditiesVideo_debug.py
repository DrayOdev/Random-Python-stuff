# This is a simple script i made that checks if the time is 20:00:00* BST which is the time you can expect a new video from the oddities roleplay* :D
# * <- means that this part can be easily changed by YOU!
import webbrowser
import datetime
import time

UPLOAD_HOUR: int = 20 # Change me to fit the upload schedule :D
UPLOAD_MINUTE: int = 0 # me as well!
CHANNEL_URL: str = "https://youtube.com/@theoddities_roleplay"  # Change for any channel you like

def Main():
    new_upload: bool = False # creates the varible that the loop is based from
    while new_upload == False:
        now = datetime.datetime.now() # DO NOT REMOVE IM VERY IMPORTANT :D
        if now.hour == UPLOAD_HOUR and now.minute == UPLOAD_MINUTE: # checks to see if it is the scheduled time for an upload
            webbrowser.open(CHANNEL_URL)
            new_upload = True # kills the loop, alternitevly remove me if you want this loop to go on forever and ever and ever.
        else:
            print("NO NEW UPLOAD", now.time()) # Uh well, im only used for debugging so uh feel free to remove me :D
            time.sleep(60) # i delay the loop by 60s

def start(): # whole thing is for syncing the script to the second. Syncing to the microsecond would require this to be a script that is ran 24/7 as it takes a while for it to sync
    start_loop: bool = False # creates the variable that the loop is based from
    while start_loop == False:
        now = datetime.datetime.now()
        if now.second == 0:
            print("STARTING") # im not required!
            start_loop = True # kills the loop!
            Main() # Calls the Main function
        else:
            print("Loop failed at: ", datetime.datetime.now().time(), "\n Attempting again in 1s") # You dont need me!
            time.sleep(1)
start() #Starts the script :D

