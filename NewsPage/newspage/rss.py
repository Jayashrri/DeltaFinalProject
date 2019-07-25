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