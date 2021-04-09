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
                        latitude = row['X'],
                        longitude = row['Y'],
                        unique_squirrel_id = row['Unique Squirrel ID'],
                        shift = row['Shift'],
                        date = datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                        age = row['Age'],
                        primary_fur_color = row['Primary Fur Color'],
                        location = row['Location'],
                        specific_location = row['Specific Location'],
                        running = convert(row['Running']),
                        chasing = convert(row['Chasing']),
                        climbing = convert(row['Climbing']),
                        eating = convert(row['Eating']),
                        foraging = convert(row['Foraging']),
                        other_activities = row['Other Activities'],
                        kuks = convert(row['Kuks']),
                        quaas = convert(row['Quaas']),
                        moans = convert(row['Moans']),
                        tail_flags = convert(row['Tail flags']),
                        tail_twitches = convert(row['Tail twitches']),
                        approaches = convert(row['Approaches']),
                        indifferent = convert(row['Indifferent']),
                        runs_from = convert(row['Runs from']),
                        )
                s.save()
            print('successfully saved csv')
        except:
            print('something wrong')
