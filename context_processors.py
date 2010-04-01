from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter

def latest_tweets( request ):
    tweets = cache.get( 'tweets' )
	
    if tweets:
        return {"tweets": tweets}

    dates = []

    tweets = twitter.Api(username='31street', password='31molor').GetUserTimeline( settings.TWITTER_USER )[0:7]
    for t in tweets:
        t.date = datetime.strptime( t.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
    cache.set( 'tweets', tweets, settings.TWITTER_TIMEOUT )

    return {"tweets": tweets, "dates": dates}
