from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):

    Latitude = models.FloatField(
        max_length=100,
        help_text=_('Latitude of the location'),
    )


    Longitude = models.FloatField(
        max_length=100,
        help_text=_('Longitude of the location'),
    )


    Squirrel_ID = models.CharField(
        max_length=20,
        help_text=_('Unique Squirrel ID'),
        primary_key=True,
        default = None,
    )
    
    AM = 'AM'
    PM = 'PM'
    
    CHOICES = [
        (AM,_('AM')),
        (PM,_('PM')),
    ]

    Shift = models.CharField(
        max_length=15,
        help_text=_('Is the sighting in the morning or in the afternoon?'),
        choices=CHOICES,
        blank=True,
    )
    
    Date = models.DateField(
        help_text=_('Click the button to select the date'),
        blank=True,
    )
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'

    AGE_CHOICES = [
        (Adult,_('Adult')),
        (Juvenile,_('Juvenile')),
    ]

    Age = models.CharField(
        max_length=15,
        help_text=_('Age'),
        choices=AGE_CHOICES,
        blank=True,
        null=True,
    )
    
    Gray = 'Gray'
    Cinnamon = 'Cinnamom'
    Black = 'Black'
    
    COLOR_CHOICES = [
        (Gray,_('Gray')),
        (Cinnamon,_('Cinnamom')),
        (Black,_('Black')),
    ]

    Primary_Fur_Color = models.CharField(
        max_length=100,
        help_text=_('Primary Fur Color'),
        choices=COLOR_CHOICES,
        blank=True,
        null=True,
    )
    
    Above_Ground = 'Above Ground'
    Ground_Plane = 'Ground Plane'

    LOCATION_CHOICES = [
        (Above_Ground,_('Above Ground')),
        (Ground_Plane,_('Ground Plane')),
    ]

    Location = models.CharField(
        max_length=20,
        help_text=_('Location'),
        choices=LOCATION_CHOICES,
        blank=True,
        null=True,
    )
    
    Specific_Location = models.CharField(
        max_length=20,
        help_text=_('Specific Location'),
        blank=True,
        null=True,
    )
    
    Running = models.BooleanField(
        help_text=_('Whether or not squirrel is running'),
        null=True,
    )
    
    Chasing = models.BooleanField(
        help_text=_('Whether or not squirrel is chasing'),
        null=True,
    )
    
    Climbing = models.BooleanField(
        help_text=_('Whether or not squirrel is climbing'),
        null=True,
    )
    
    Eating = models.BooleanField(
        help_text=_('Whether or not squirrel is eating'),
        null=True,
    )
    
    Foraging = models.BooleanField(
        help_text=_('Whether or not squirrel is foraging'),
        null=True,
    )
    

    Other_Activities = models.CharField(
        max_length=100,
        help_text=_('Please sepecify other activities you saw'),
        blank=True,
        null=True,
    )
    
    Kuks = models.BooleanField(
        help_text=_('Kuks'),
        null=True,
    )
    
    Quaas = models.BooleanField(
        help_text=_('Quaas'),
        null=True,
    )
    
    Moans = models.BooleanField(
        help_text=_('Moans'),
        null=True,
    )
    
    Tail_Flags = models.BooleanField(
        help_text=_("Whether or not squirrel's tail flag"),
        null=True,
    )
    
    Tail_Twitches = models.BooleanField(
        help_text=_("Whether or not squirrel's tail twitch"),
        null=True,
    )

    Approaches = models.BooleanField(
        help_text=_('Whether or not squirrel approaches'),
        null=True,
    )
    
    Indifferent = models.BooleanField(
        help_text=_('Whether or not squirrel is indifferent'),
        null=True,
    )

    Runs_From = models.BooleanField(
        help_text=_('Where the squirrel is running from'),
        null=True,
    )

    def __str__(self):
        return self.Squirrel_ID


