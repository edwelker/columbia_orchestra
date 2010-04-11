from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter
import re


def latest_tweets( request ):
    tweets = cache.get( 'tweets' )
    
    if tweets:
        return {"tweets": tweets}

    dates = []
    pattern = r'''\b((?:(?:http)://|www\.)[-a-zA-Z0-9+&@#/%=~_|$?!:,.]*[a-zA-Z0-9+&@#/%=~_|$])'''
    replacement = '<a href="\\1">\\1</a>'

    api = twitter.Api()
    tweets = api.GetUserTimeline( settings.TWITTER_USER, count=2 )
    for t in tweets:
        t.date = datetime.strptime( t.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
        t.text = re.sub(pattern, replacement, t.text)
    cache.set( 'tweets', tweets, settings.TWITTER_TIMEOUT )

    return {"tweets": tweets, "dates": dates}
