import feedparser

def GetFeed(FeedObj):
    Feed=feedparser.parse(FeedObj.url)
    return Feed
