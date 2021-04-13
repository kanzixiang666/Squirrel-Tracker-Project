# Squirrel-Tracker-Project
This is IEOR4501 Final Project, our goal is to show the squirrels in NYC central park in map and let people to update the data.

The project is based on Django and we implement several features:
  1. Management commands to import squirrel data from csv file and to export updated data to local path.
    - The file path should be specified at the command line after the name of the management command. 
    - $ python manage.py import_squirrel_data /path/to/file.csv
    - $ python manage.py export_squirrel_data /path/to/file.csv
  
  2. Views
    - A map displayed the last viewed location of squirrels on an OpenStreet Map 
    - located at: /sightings/maps 
    
    - A view that lists all squirrel sightings with links to view each sightings 
    - located at: /sightings/data
    
    - A page that shows statistics about all squirrels
    - located at: /sightings/stat 
    
    - A page that allows users to add a new squirrel with information
    - located at: /sightings/add
    
    - Urls in squirrel id format that allows users to update information of a specific squirrel
    - located at: /sightings/<specific squirrel id> 
    
    