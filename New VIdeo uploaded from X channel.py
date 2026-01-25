import feedparser, webbrowser, datetime, time

CHANNEL_ID = ""
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

while True:
    CHANNEL_ID = input("Please enter the channel ID: ")
    if CHANNEL_ID == "":
        break
    else:
        feed = feedparser.parse(RSS_URL)
        if feed.entries:
            latest = feed.entries[0] # gets video
            if datetime.date(*latest.published_parsed[:3]) == datetime.date.today(): # checks upload date
                webbrowser.open(latest.link) # opens link
                break # closes sctipt
        print("Video not uploaded")
        time.sleep(300) # 5 min delay before next check.
