import feedparser
from newspaper import Article

def GetFeed(FeedObj):
    Feed=feedparser.parse(FeedObj.url)
    return Feed

def GetArticle(FeedLink):
    newarticle=Article(FeedLink)
    newarticle.download()
    newarticle.parse()
    return newarticle
