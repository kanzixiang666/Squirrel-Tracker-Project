from django.core.management.base import BaseCommand
from sightings.models import Squirrel
from datetime import datetime
import csv 

class Command(BaseCommand):

    help = 'Export the squirrel data for project'

    def add_arguments(self,parser):
        parser.add_argument('path',type=str)


    def handle(self,*args,**kwargs):
    	
    	try:
    		with open(kwargs['path'], 'w', encoding = 'utf-8') as f:
    			# create csv writer
    			header = [ 'X',
    					   'Y',
    					   'Unique Squirrel ID',
    					   'Shift',
    					   'Date',
    					   'Age',
    					   'Primary Fur Color',
    					   'Location',
    					   'Specific Location',
    					   'Running',
    					   'Chasing',
    					   'Climbing',
    					   'Eating',
    					   'Foraging',
    					   'Other Activities',
    					   'Kuks',
    					   'Quaas',
    					   'Moans',
    					   'Tail flags',
    					   'Tail twitches',
    					   'Approaches',
    					   'Indifferent',
    					   'Runs from'
    					   ]

    			writer = csv.DictWriter(f, fieldnames=header)
    			#write the header
    			writer.writeheader()

    			squirrels = Squirrel.objects.all().values()
    			
    			#get every attribute of a squirrel
    			for i in squirrels:
    				X = i['Longitude']
    				Y = i['Latitude']
    				unique_id = i['Squirrel_ID']
    				Shift = i['Shift']
    				Date = i['Date'].strftime("%m%d%Y")
    				Age = i['Age']
    				Col = i['Primary_Fur_Color']
    				Location = i['Location']
    				Specific_Location = i['Specific_Location']
    				Running = i['Running']
    				Chasing = i['Chasing']
    				Climbing = i['Climbing']
    				Eating = i['Eating']
    				Foraging = i['Foraging']
    				Other_Activities = i['Other_Activities']
    				Kuks = i['Kuks']
    				Quaas = i['Quaas']
    				Moans = i['Moans']
    				Tail_Flags = i['Tail_Flags']
    				Tail_Twitches = i['Tail_Twitches']
    				Approaches = i['Approaches']
    				Indifferent = i['Indifferent']
    				Runs_From = i['Runs_From']

    				# write into csv row
    				writer.writerow({
    					'X':X,
    					'Y':Y,
    					'Unique Squirrel ID':unique_id,
    					'Shift':Shift,
    					'Date':Date,
    					'Age':Age,
    					'Primary Fur Color':Col,
    					'Location':Location,
    					'Specific Location':Specific_Location,
    					'Running':Running,
    					'Chasing':Chasing,
    					'Climbing':Climbing,
    					'Eating':Eating,
    					'Foraging':Foraging,
    					'Other Activities':Other_Activities,
    					'Kuks':Kuks,
    					'Quaas':Quaas,
    					'Moans':Moans,
    					'Tail flags':Tail_Flags,
    					'Tail twitches':Tail_Twitches,
    					'Approaches':Approaches,
    					'Indifferent':Indifferent,
    					'Runs from':Runs_From
    					})

    			print("data successfully downloaded to csv!")
   				
    	except:
    		print('something wrong')


