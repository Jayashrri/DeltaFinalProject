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
    return newarticle

def GetUpdate(UserView):
    if (UserView.last_viewed):
        FeedObj=UserView.site_name
        Feed=feedparser.parse(FeedObj.url)
        entry=Feed.entries[0].published_parsed
        lasttime=UserView.last_viewed.timetuple()
        if (entry > lasttime):
            return 1
        else:
            return 0
    else:
        return 1
