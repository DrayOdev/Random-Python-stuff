# This is a simple script i made that checks if the time is 20:00:00* BST which is the time you can expect a new video from the oddities roleplay* :D
# * <- means that this part can be easily changed by YOU!
import webbrowser
import datetime
import time

UPLOAD_HOUR = 20 # Change me to fit the upload schedule :D
UPLOAD_MINUTE = 0 # and me as well!
CHANNEL_URL = "https://youtube.com/@theoddities_roleplay" # Change for any channel you like

def run():
    new_upload: bool = False
    while new_upload == False:
        if datetime.datetime.now().hour == UPLOAD_HOUR and datetime.datetime.now().minute == UPLOAD_MINUTE: # checks to see if it is the scheduled time for an upload
            webbrowser.open(CHANNEL_URL)
            new_upload = True # kills the loop, alternitevly remove me if you want this loop to go on forever and ever and ever.
        else:
            now = datetime.datetime.now() # resets time for the print can be removed
            print("NO NEW UPLOAD", now.time()) # so can i! if you dont want me spamming the console all day!
            time.sleep(60) # delays the loop by 60s

def start(): # whole thing is for syncing the script to the second (NOT MILLISECOND but i could totally do that.)
    start_loop: bool = False # creates the variable that the loop is based from
    while start_loop == False:
        now = datetime.datetime.now()
        if now.second == 0:
            print("STARTING") # Im not required 
            start_loop = True # kills the loop!
            run() # calls the main part of the script could have called this main instead of run!
        else:
            print("Loop failed at: ", datetime.datetime.now().time(), "\n Attempting again in 1s") # You dont need me!
            time.sleep(1)
start() # kickstarts the script :D



