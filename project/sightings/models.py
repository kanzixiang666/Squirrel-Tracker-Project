from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Squirrel(models.Model):

    latitude = models.FloatField(
            help_text = _('latitude'),
            )

    longitude = models.FloatField(
            help_text = _('longitude'),
            )

    squirrel_id = models.CharField(
            max_length=25,
            help_text = _('unique id of the squirrel'),
            )

    AM = 'AM'
    PM = 'PM'

    shift_choices=[
            (AM,_('AM')),
            (PM,_('PM')),
             ]
    
    shift = models.CharField(
            max_length=5,
            help_text=_('shift'),
            choices=shift_choices,
            )
    
    date = models.DateField(
            help_text=_('date'),
            )

    
    adult = 'Adult'
    baby = 'Baby'
    unknown = 'Unknown'

    age_choices = [
            (adult,_('Adult')),
            (baby,_('Baby')),
            (unknown,_('Unknown')),
            ]

    age = models.CharField(
            max_length=15,
            help_text=_('age of the squirrel'),
            choices=age_choices,
            )

    grey = 'Grey'
    blond = 'Blond'
    black = 'Black'
    white = 'White'

    color_choices = [
           (grey,_('Grey')),
           (blond,_('Blond')),
           (black,_('Black')),
           (white,_('White')),
           ]

    primary_fur_color = models.CharField(
            max_length=15,
            help_text=_('primary fur color'),
            choices = color_choices,
            )

    above_tree = 'above tree'
    above_ground = 'above ground'
    
    location_choices = [
            (above_tree,_('above tree')),
            (above_ground,_('above ground')),
            (unknown,_('unknown')),
            ]

    location = models.CharField(
            max_length=25,
            help_text=_('location'),
            choices=location_choices,
            default=unknown,
            )

    specific_location = models.CharField(
            max_length=50,
            help_text=_('specific location'),
            blank=True,)

    running = models.BooleanField(
            help_text=_('running'),
            default=False,
            )

    chasing = models.BooleanField(
            help_text=_('chasing'),
            default=False,
            )

    climbing = models.BooleanField(
            help_text=_('climbing'),
            default=False,
            )

    eating = models.BooleanField(
            help_text=_('eating'),
            default=False,
            )

    foraging = models.BooleanField(
            help_text=_('foraging'),
            default=False,
            )

    other_activities = models.CharField(
            max_length=50,
            help_text=_('other activities'),
            blank=True,
            )
    kuks = models.BooleanField(
           help_text = _('Kuks'),
           default=False,
            )

    quaas = models.BooleanField(
           help_text = _('Quaas'),
           default=False,
            )

    moans = models.BooleanField(
           help_text = _('Moans'),
           default=False,
            )

    tail_flags = models.BooleanField(
            help_text = _('Tail Flags'),
            default=False,
            )

    tail_twitches = models.BooleanField(
            help_text = _('Tail Twitches'),
            default=False,
            )

    approaches = models.BooleanField(
            help_text = _('Approaches'),
            default=False,
            )

    indifferent = models.BooleanField(
            help_text = _('Indifferent'),
            default=False,
            )

    runs_from = models.BooleanField(
            help_text = _('Runs From'),
            default=False,
            )

    def __str__(self):
        return "squirrel: "+str(self.squirrel_id)
