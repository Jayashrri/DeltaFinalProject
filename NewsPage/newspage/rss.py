import feedparser
from newspaper import Article, Config
from datetime import datetime

def GetFeed(FeedObj):
    Feed=feedparser.parse(FeedObj.url)
    return Feed

def GetArticle(FeedLink,request):
    user_agent=request.META['HTTP_USER_AGENT']
    config=Config()
    config.browser_user_agent=user_agent
    newarticle=Article(FeedLink,config=config)
    newarticle.download()
    newarticle.parse()
    newarticle.nlp()
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
