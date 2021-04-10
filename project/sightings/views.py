from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

# Create your views here.
#take request and hand back response
def index(request):

    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels
            }

    return render(request, 'sightings/index.html',context)



