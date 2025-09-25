# This is a simple script i made that checks (in prolly a really dumb way) if the time is 20:00:00 BST which is the time you can expect a new video from the oddities roleplay :D
import webbrowser
import datetime
import time

def run():
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 0: # checks if its upload time
        webbrowser.open("https://youtube.com/@theoddities_roleplay") # opens their channel
    else: # not the time for an upload
        print("NO NEW UPLOAD") 
        time.sleep(60) # waits 60s before calling the run() function
        run()

def start(): # do i really need to add comments to all this?
    start_loop: bool = False
    if datetime.datetime.now().second == 0 and start_loop == False: # so the script syncs with real time and so line 11 wont cause issues due to desync 
        print("STARTING")
        start_loop = True
        run()
    elif start_loop == False:
        print("Loop failed trying again in 1s")
        time.sleep(1)
        start()
start()

