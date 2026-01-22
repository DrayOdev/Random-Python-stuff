import requests, re, webbrowser, datetime, time

UPLOAD_HOUR: int = 0
UPLOAD_MINUTE: int = 53
channel_url: str
loop: bool = False

def Main():
    channel_url = input("Please enter a channel URL: ")    
    if channel_url != "":
        loop = True
    
    while loop:
        now = datetime.datetime.now()
        if now.hour == UPLOAD_HOUR and now.minute == UPLOAD_MINUTE:
            html = requests.get(channel_url + "/videos").text
            url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
            webbrowser.open(url)
            break
        else:
            time.sleep(60 - now.second)

Main()
