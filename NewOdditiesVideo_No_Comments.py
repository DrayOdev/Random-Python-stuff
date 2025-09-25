import webbrowser, datetime, time

UPLOAD_HOUR: int = 20 
UPLOAD_MINUTE: int = 0 
CHANNEL_URL: str = "https://youtube.com/@theoddities_roleplay"

def Main():
    while True:
        now = datetime.datetime.now()
        if now.hour == UPLOAD_HOUR and now.minute == UPLOAD_MINUTE:
            webbrowser.open(CHANNEL_URL) 
            break
        else:
            time.sleep(60 - now.second)

Main()

