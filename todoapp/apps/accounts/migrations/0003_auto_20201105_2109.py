# Generated by Django 3.1.2 on 2020-11-05 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201022_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='trello_api_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='trello_api_secret',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
