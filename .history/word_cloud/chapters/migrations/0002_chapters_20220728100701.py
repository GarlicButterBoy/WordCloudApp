# Generated by Django 4.0.6 on 2022-07-28 14:05

from django.db import migrations

def create_data(apps, schema_editor):
    Chapter = apps.get_model('chapters', 'Chapter')

class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0001_initial'),
    ]

    operations = [
    ]
