from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from orch.meet_the_orchestra.models import OrchestraMember

# Create your views here.
def all_members(request):
    m = OrchestraMember.objects.exclude(noncurrent_member=True).order_by('instrument', '-principal', 'last_name')
    
    cut = ['Cello']
    
    return render_to_response('members.html', {'members': m, 'cut': cut})

def member(request, first_name, last_name):
    m = get_object_or_404(OrchestraMember, first_name__iexact=first_name, last_name__iexact=last_name)
    return render_to_response('member.html', {'member': m})