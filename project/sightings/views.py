from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Squirrel

# Create your views here.
#take request and hand back response
def index(request):

    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }

    
    return render(request, 'sightings/index.html',context)

def detail(request,unique_squirrel_id):
    
    squirrel = get_object_or_404(Squirrel, pk = unique_squirrel_id)
    context = {
            'squirrel':squirrel,
            }

    return render(request, 'sightings/detail.html',context)

def stats(request):
    #get all squirrels
    squirrels = Squirrel.objects.all()
    #total number
    total = squirrels.count()
    #age
    Adult_n = squirrels.filter(age='Adult').count()
    Juvenile_n = squirrels.filter(age='Juvenile').count()
    #Shift
    AM_n = squirrels.filter(shift='AM').count()
    PM_n = squirrels.filter(shift='PM').count()
    #Location 
    above_ground_n = squirrels.filter(location='Above Ground').count()
    ground_plane_n = squirrels.filter(location='Ground Plane').count()
    #fur color
    grey_n = squirrels.filter(primary_fur_color='Grey').count()
    clinamon_n = squirrels.filter(primary_fur_color='Clinamon').count()
    black_n = squirrels.filter(primary_fur_color = 'Black').count()

    context = {
            'total':total,
            'Adult_n':Adult_n,
            'Juvenile_n':Juvenile_n,
            'AM_n':AM_n,
            'PM_n':PM_n,
            'above_ground_n':above_ground_n,
            'ground_plane_n':ground_plane_n,
            'grey_n':grey_n,
            'clinamon_n':clinamon_n,
            'black_n':black_n,
            }

    return render(request, 'sightings/stats.html',context)





