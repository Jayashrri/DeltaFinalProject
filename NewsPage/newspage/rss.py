import feedparser
from newspaper import Article
from datetime import datetime

def GetFeed(FeedObj):
    Feed=feedparser.parse(FeedObj.url)
    return Feed

def GetArticle(FeedLink):
    newarticle=Article(FeedLink)
    newarticle.download()
    newarticle.parse()
    return newarticle

def CheckUpdate(FeedObj):
    if (FeedObj.last_update):
        Feed=feedparser.parse(FeedObj.url)
        entry=Feed.entries[0].published_parsed
        lasttime=FeedObj.last_update.timetuple()
        if (entry > lasttime):
            return 1
        else:
            return 0
    else:
        return 1
