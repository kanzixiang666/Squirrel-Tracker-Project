# Squirrel Tracker

## Introduction
#### This is Columbia University IEOR4501 Final Project, our goal is to show the squirrels in NYC central park in map and let people to update the data! 

![](https://www.pestremovalguide.com/wp-content/uploads/2015/08/squirrel_garden.jpg)

## Link 
Here's our app link:
https://ieor4523-data-analytics-303114.df.r.appspot.com/ 
(Sometimes the website is down because Google suspends it...)

## Authors 
#### <li> Xiaohan Yang (yxh0082)</li>
#### <li> Zixiang Kan (kanzixiang666)</li>


## Group
<li> Project Group 4, Section 001 </li>
  
  
## UNIs 
<li> [xy2469, zk2244] </li>
    
   
   
## The project is based on Django and we implement several features:

### 1.Management commands 

Allow users to import squirrel data from csv file and to export updated data to local path.

The file path should be specified at the command line after the name of the management command. 

#### import command:
    - $ python manage.py import_squirrel_data /path/to/file.csv
#### export command:
    - $ python manage.py export_squirrel_data /path/to/file.csv
  
#### 2. Views
A map displayed the last viewed location of squirrels on an OpenStreet Map. Squirrels are cute!
    
    - located at: /sightings/maps 
    
    
A page that lists all squirrel sightings with links to view each sightings 
    
    - located at: /sightings/data
    
    
A page that shows statistics about all squirrels
    
    - located at: /sightings/stat 
    
    
A page that allows users to add a new squirrel with information
    
    - located at: /sightings/add
    
    
Clicking squirrel's id allows users to update information of a specific squirrel!
    
    - located at: /sightings/<specific squirrel id> 
    

#### Photo Reference: 
How To Protect Your Garden From Squirrels
https://www.pestremovalguide.com/how-to-protect-your-garden-from-squirrels/ Access April 13 2021 
