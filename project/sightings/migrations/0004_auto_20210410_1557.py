# Generated by Django 3.1.7 on 2021-04-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20210409_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='primary_fur_color',
            field=models.CharField(choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Clinamon', 'Clinamon')], help_text='primary fur color', max_length=15),
        ),
    ]