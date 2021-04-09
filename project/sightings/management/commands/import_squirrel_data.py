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

            def convert(string):
                if string in ('false','FALSE','False'):
                    return False
                elif string in ('true','TRUE','True'):
                    return True:
                else:
                    return None

            for row in data:
                s = Squirrel(
                        latitude = row['X'],
                        longitude = row['Y'],
                        squirrel_id = row['Unique Squirrel ID'],
                        shift = row['shift'],
                        date = datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                        )
        except:
            print('something wrong')
