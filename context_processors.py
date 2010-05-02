from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter, feedparser
import re
from dateutil.parser import parse
from django.http import HttpResponseServerError


def latest_tweets( request ):
    tweets = cache.get( 'tweets' )
    
    if tweets:
        return {"tweets": tweets}

    dates = []
    pattern = r'''\b((?:(?:http)://|www\.)[-a-zA-Z0-9+&@#/%=~_|$?!:,.]*[a-zA-Z0-9+&@#/%=~_|$])'''
    replacement = '<a href="\\1">\\1</a>'

    api = twitter.Api()
    try:
        tweets = api.GetUserTimeline( settings.TWITTER_USER, count=2 )
        for t in tweets:
            t.date = datetime.strptime( t.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
            t.text = re.sub(pattern, replacement, t.text)
        cache.set( 'tweets', tweets, settings.TWITTER_TIMEOUT )
    except:
        return HttpResponseServerError('Twitter failure')

    return {"tweets": tweets, "dates": dates}


def latest_facebook( request ):
    
    feed = feedparser.parse('http://www.facebook.com/feeds/page.php?format=atom10&id=211864312316')
    
    fb = feed['entries'][0:1]
    #dates = [parse(d.published) for d in fb]
    
    for entry in fb:
        entry['fixed_date'] = parse(entry.published)
    
    return { 'fb': fb }