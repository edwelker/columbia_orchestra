from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter, feedparser
import re
from dateutil.parser import parse
from django.http import HttpResponseServerError

pattern = r'''\b((?:(?:http)://|www\.)[-a-zA-Z0-9+&@#/%=~_|$?!:,.]*[a-zA-Z0-9+&@#/%=~_|$])'''
replacement = '<a href="\\1">\\1</a>'

def latest_tweets( request ):
    tweets = cache.get( 'tweets' )
    
    if tweets:
        return {"tweets": tweets}

    dates = []

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
    fb = cache.get( 'fb' )
    
    if fb: 
        return {'fb': fb}

    try:
        feed = feedparser.parse('http://www.facebook.com/feeds/page.php?format=atom10&id=211864312316')    
        fb = feed['entries'][0:2]
        #dates = [parse(d.published) for d in fb]
    
        for entry in fb:
            entry['published'] = parse(entry.published)
            entry['title'] = re.sub(pattern, replacement, entry.title)
            
        cache.set( 'fb', fb, settings.TWITTER_TIMEOUT )    
    except:
        return HttpResponseServerError('Facebook failure')
    
    return { 'fb': fb }