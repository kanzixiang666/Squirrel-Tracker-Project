from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#take request and hand back response
def index(request):
    return render(request, 'sightings/index.html',{})



