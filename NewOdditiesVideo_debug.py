# This is a simple script i made that checks if the time is 20:00:00* BST which is the time you can expect a new video from the oddities roleplay* :D
# * <- means that this part can be easily changed by YOU!
import webbrowser, datetime, time

UPLOAD_HOUR: int = 20 # Change me to fit the upload schedule :D
UPLOAD_MINUTE: int = 0 # me as well!
CHANNEL_URL: str = "https://youtube.com/@theoddities_roleplay"  # Change for any channel you like

def Main():
    while True:
        now = datetime.datetime.now()
        if now.hour == UPLOAD_HOUR and now.minute == UPLOAD_MINUTE: # if it is the scheduled time for an upload
            webbrowser.open(CHANNEL_URL)
            print("NEW UPLOAD, OPENING CHANNEL")
            break # kills the loop
        else:
            print("NO NEW UPLOAD")
            time.sleep(60 - now.second) # i delay the loop by 60s

Main() #Starts the script :D

