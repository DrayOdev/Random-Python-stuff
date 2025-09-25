import requests, re, webbrowser, datetime, time

UPLOAD_HOUR: int = 0
UPLOAD_MINUTE: int = 53
CHANNEL_URL: str = "https://youtube.com/@theoddities_roleplay"

def Main():
    while True:
        now = datetime.datetime.now()
        if now.hour == UPLOAD_HOUR and now.minute == UPLOAD_MINUTE:
            html = requests.get(CHANNEL_URL + "/videos").text
            url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
            webbrowser.open(url)
            break
        else:
            time.sleep(60 - now.second)

Main()
