import webbrowser
import datetime
import time

def run():
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 0:
        webbrowser.open("https://youtube.com/@theoddities_roleplay")
    else:
        print("NO NEW UPLOAD")
        time.sleep(60)
        run()

def start():
    start_loop: bool = False
    if datetime.datetime.now().second == 0 and start_loop == False:
        print("STARTING")
        start_loop = True
        run()
    elif start_loop == False:
        print("Loop failed trying again in 1s")
        time.sleep(1)
        start()
start()
