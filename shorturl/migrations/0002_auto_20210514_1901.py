# Generated by Django 3.0.5 on 2021-05-14 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='time_to_delete',
        ),
        migrations.AddField(
            model_name='url',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
