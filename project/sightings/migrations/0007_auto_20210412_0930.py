# Generated by Django 3.2 on 2021-04-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0006_alter_squirrel_primary_fur_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Latitude',
            field=models.FloatField(help_text='Latitude of the location', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Longitude',
            field=models.FloatField(help_text='Longitude of the location', max_length=100),
        ),
    ]
