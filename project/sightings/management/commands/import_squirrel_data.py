from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import datetime
import csv 

class Command(BaseCommand):

    help = 'Import the squirrel data for project'
    
    def add_arguments(self,parser):
        parser.add_argument('path',type=str)

    def handle(self,*args,**kwargs):
        path = kwargs['path']

        try:
            with open(path,encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
                print(data[100])

        except:
            print('something wrong')
