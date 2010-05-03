from django.shortcuts import render_to_response, get_object_or_404
import datetime
from events.models import Event, Season, Location, Soloist

# Create your views here.
def view_single_event(request):
	myevent, curSeason = get_single_event()
	return render_to_response('single_event.html', {'event': myevent, 'season': curSeason })
    
def view_specific_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    season = get_current_season()
    return render_to_response('single_event.html', {'event': event, 'season': season})
	
def view_current_season(request):
	curSeason, curSeasonName = get_current_seasonEvents_and_Name()
	return render_to_response('season.html', { 'season': curSeason, 'seasonname': curSeasonName })
	
def view_season(request, slug):
	season = get_object_or_404(Season, slug=slug)
	events = Event.objects.filter(season__name__exact=season.name)
	return render_to_response('season.html', { 'season': events, 'seasonname': season.name })
	
def all_locations(request):
	locations = Location.objects.filter()
	return render_to_response('locations.html', { 'locations': locations })
	
def single_location(request, slug):
	location = get_object_or_404(Location, slug__iexact=slug)
	return render_to_response('single_location.html', { 'location': location })
	
#NEED: to be fixed so that soloist_events and season_soloists are in one iterable list.	
def all_soloists(request):
	curSeason = get_current_season()
	season_soloists = Soloist.objects.filter(season=curSeason)
	return render_to_response('soloists.html', { 'soloists': season_soloists, 'season': curSeason })
	
def single_soloist(request, slug):
	soloist = get_object_or_404(Soloist, slug=slug)
	#array of events... becuase Soloists can do more than one concert
	events = soloist.event_set.all()
	return render_to_response('single_soloist.html', { 'soloist': soloist, 'events': events })
	
	
#def home_page(request):
#	myevent, curSeason = get_single_event()
#	now = datetime.datetime.now
#	urgent = Item.objects.filter(priority=6, expires__gte=now)
#	#get anything of Audition or High Priority
#	myitems = Item.objects.filter(priority__lt=6, priority__gte=4, expires__gte=now)
#	return render_to_response('events/homepage.html', {'items' : myitems, 'event': myevent, 'season': curSeason, 'urgent': urgent })	
	
	
#big helpers	
def get_single_event():
	#NEED: to make sure that if the season goes out of date, that we still display the last thing on the homepage!!!!
	
	#Seasons sort by date
	today = datetime.date.today()
	curSeason = Season.objects.filter(startdate__lte=today, enddate__gte=today)
	curSeason = Season() if (len(curSeason) == 0) else curSeason[0]
	#Events sort by datetimes
	myevent = Event.objects.filter(season__name__exact=curSeason.name, date__gte=datetime.datetime.today())
	myevent = Event() if (len(myevent) == 0) else myevent[0]
	return(myevent, curSeason)
	
def get_current_seasonEvents_and_Name():
	today = datetime.date.today()
	curSeason = Season.objects.filter(startdate__lte=today, enddate__gte=today)
	curSeason = Season() if (len(curSeason) == 0) else curSeason[0]
	curSeasonName = curSeason.name
	curSeasonEvents = Event.objects.filter(season__name__exact=curSeason.name)
	return (curSeasonEvents, curSeasonName)
	
#little helpers
def get_current_season():
	today = datetime.date.today()
	curSeason = Season.objects.filter(startdate__lte=today, enddate__gte=today)
	curSeason = Season() if (len(curSeason) == 0) else curSeason[0]
	return curSeason
