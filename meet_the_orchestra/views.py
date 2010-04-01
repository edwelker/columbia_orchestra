from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from orch.meet_the_orchestra.models import OrchestraMember

# Create your views here.
def all_members(request):
    m = OrchestraMember.objects.all().order_by('instrument')
    return render_to_response('members/members.html', {'members': m })

def member(request, member_id):
    m = get_object_or_404(OrchestraMember, pk=member_id)
    return render_to_response('members/member.html', {'member': m})