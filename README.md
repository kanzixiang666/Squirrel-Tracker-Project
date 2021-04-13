# Squirrel-Tracker-Project

### This is IEOR4501 Final Project, our goal is to show the squirrels in NYC central park in map and let people to update the data.

![test image size](https://images.immediate.co.uk/production/volatile/sites/23/2015/11/GettyImages-948163948-6f26c98.jpg?quality=90&crop=95px%2C231px%2C2132px%2C1420px&resize=620%2C413)

![](https://www.pestremovalguide.com/wp-content/uploads/2015/08/squirrel_garden.jpg)


## The project is based on Django and we implement several features:


### 1.Management commands 

Allow users to import squirrel data from csv file and to export updated data to local path.

The file path should be specified at the command line after the name of the management command. 
#### import command:
    - $ python manage.py import_squirrel_data /path/to/file.csv
#### export command:
    - $ python manage.py export_squirrel_data /path/to/file.csv
  
### 2. Views
A map displayed the last viewed location of squirrels on an OpenStreet Map 
    
    - located at: /sightings/maps 
    
A view that lists all squirrel sightings with links to view each sightings 
    
    - located at: /sightings/data
    
A page that shows statistics about all squirrels
    
    - located at: /sightings/stat 
    
A page that allows users to add a new squirrel with information
    
    - located at: /sightings/add
    
Urls in squirrel id format that allows users to update information of a specific squirrel
    
    - located at: /sightings/<specific squirrel id> 
    
    
