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

            def convert(string):
                if string in ['false','FALSE','False']:
                    return False
                elif string in ['true','TRUE','True']:
                    return True
                else:
                    return None

            for row in data:
                s = Squirrel(
                        Latitude = row['Y'],
                        Longitude = row['X'],
                        Squirrel_ID = row['Unique Squirrel ID'],
                        Shift = row['Shift'],
                        Date = datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                        Age = row['Age'],
                        Primary_Fur_Color = row['Primary Fur Color'],
                        Location = row['Location'],
                        Specific_Location = row['Specific Location'],
                        Running = convert(row['Running']),
                        Chasing = convert(row['Chasing']),
                        Climbing = convert(row['Climbing']),
                        Eating = convert(row['Eating']),
                        Foraging = convert(row['Foraging']),
                        Other_Activities = row['Other Activities'],
                        Kuks = convert(row['Kuks']),
                        Quaas = convert(row['Quaas']),
                        Moans = convert(row['Moans']),
                        Tail_Flags = convert(row['Tail flags']),
                        Tail_Twitches = convert(row['Tail twitches']),
                        Approaches = convert(row['Approaches']),
                        Indifferent = convert(row['Indifferent']),
                        Runs_From = convert(row['Runs from'])
                        )
                s.save()
            print('successfully saved csv')
        except:
            print('something wrong')
