from django.core.management.base import BaseCommand
import csv
from sightings.models import Squirrel
import datetime

class Command(BaseCommand):
    help = 'Import the squirrel data for project'
    
    def add_arguments(self,parser):
        parser.add_argument('path',type=str)

    def handle(self,*args,**kwargs):
        path = kwargs['path']
   
    try:
        with open(path,encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row['X'])
            
