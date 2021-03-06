# Generated by Django 3.2 on 2021-04-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('X', models.FloatField(help_text='Latitude', max_length=10)),
                ('Y', models.FloatField(help_text='Longitude', max_length=10)),
                ('Squirrel_ID', models.CharField(default=None, help_text='Unique Squirrel ID', max_length=100, primary_key=True, serialize=False)),
                ('Shift', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=100)),
                ('Date', models.DateField(blank=True, help_text='Date')),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age', max_length=15, null=True)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamom', 'Cinnamom'), ('Black', 'Black')], help_text='Primary Fur Color', max_length=100, null=True)),
                ('Location', models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], help_text='Location', max_length=100, null=True)),
                ('Specific_Location', models.CharField(blank=True, help_text='Specific Location', max_length=100, null=True)),
                ('Running', models.BooleanField(help_text='Whether or not squirrel is running', null=True)),
                ('Chasing', models.BooleanField(help_text='Whether or not squirrel is chasing', null=True)),
                ('Climbing', models.BooleanField(help_text='Whether or not squirrel is climbing', null=True)),
                ('Eating', models.BooleanField(help_text='Whether or not squirrel is eating', null=True)),
                ('Foraging', models.BooleanField(help_text='Whether or not squirrel is foraging', null=True)),
                ('Other_Activities', models.CharField(blank=True, help_text='Other Activities', max_length=100, null=True)),
                ('Kuks', models.BooleanField(help_text='Kuks', null=True)),
                ('Quaas', models.BooleanField(help_text='Quaas', null=True)),
                ('Moans', models.BooleanField(help_text='Moans', null=True)),
                ('Tail_Flags', models.BooleanField(help_text="Whether or not squirrel's tail flag", null=True)),
                ('Tail_Twitches', models.BooleanField(help_text="Whether or not squirrel's tail twitch", null=True)),
                ('Approaches', models.BooleanField(help_text='Whether or not squirrel approaches', null=True)),
                ('Indifferent', models.BooleanField(help_text='Whether or not squirrel is indifferent', null=True)),
                ('Runs_From', models.BooleanField(help_text='Where the squirrel is running from', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AdoptRequest',
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
    ]
