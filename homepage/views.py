from orch.meet_the_orchestra.models import OrchestraMember
from orch.homepage.models import Event
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime

# Create your views here.

def home(request):
    m = OrchestraMember.objects.all()[0] #will be changed be randomized later
    e = Event.objects.filter(date__gte=datetime.datetime.today()).order_by("date")[0]
    
    return render_to_response('home.html', {'member': m, 'event': e}, context_instance=RequestContext(request))