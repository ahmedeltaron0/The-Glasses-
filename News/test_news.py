import feedparser

# Example RSS feed URL for "world news"
rss_url = 'https://news.google.com/rss/search?q=world+news&hl=en-US&gl=US&ceid=US:en'

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Loop through the entries and print the title and link
for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}\n")
