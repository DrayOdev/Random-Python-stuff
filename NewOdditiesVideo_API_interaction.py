import feedparser, webbrowser, datetime, time

CHANNEL_ID = "UC2NVEa8NLT0sZA5v1tVatqQ"
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

while True:
    feed = feedparser.parse(RSS_URL)
    if feed.entries:
        latest = feed.entries[0] # gets video
        if datetime.date(*latest.published_parsed[:3]) == datetime.date.today(): # checks upload date
            webbrowser.open(latest.link) # opens link
            break # closes sctipt
    print("Video not uploaded")
    time.sleep(300) # 5 min delay before next check.

# we dont need to be accurate anymore as we aren't tied to a schedule rather we are tied to the Channel ID which is a tad annoying to get but not too bad
