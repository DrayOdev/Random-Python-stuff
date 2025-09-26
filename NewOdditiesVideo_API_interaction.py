import feedparser, webbrowser, datetime, time

CHANNEL_ID = "UC2NVEa8NLT0sZA5v1tVatqQ"
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

def main():
    while True:
        now = datetime.datetime.now()
        feed = feedparser.parse(RSS_URL) # finds the feed based on the Channel
        latest_video = feed.entries[0] # gets the latest video
        uploaded = datetime.date(*latest_video.published_parsed[:3]) # gets the day it was uploaded
        if uploaded == now.date(): # checks if it was uploaded today
            latest_video = feed["entries"][0].link # gets the link
            webbrowser.open(latest_video) # opens the link
            break # closes the script
        else:
            print("Video not uploaded")
            time.sleep(300) # waits 5 min

main()

# we dont need to be accurate anymore as we aren't tied to a schedule rather we are tied to the Channel ID which is a tad annoying to get but not too bad
