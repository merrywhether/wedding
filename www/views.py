from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    return render_to_response('index.html', {}, RequestContext(request))

def accommodations(request):
    return render_to_response('accommodations.html', {}, RequestContext(request))