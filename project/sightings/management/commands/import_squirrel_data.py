from django.core.management.base import BaseCommand
import csv
import datetime

class Command(BaseCommand):
    help = 'Import the squirrel data for project'
    
    def add_arguments(self,parser):
        parser.add_argument('path',type=str)

    def handle(self,*args,**kwargs):
        path = kwargs['path']
        print(path)
