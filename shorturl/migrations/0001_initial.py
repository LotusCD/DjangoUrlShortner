# Generated by Django 3.0.5 on 2021-05-19 03:03

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('long', models.CharField(default='', max_length=1000)),
                ('short', models.CharField(default='', max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire_at', models.IntegerField(default=1621393730124)),
                ('ip', models.CharField(default='', max_length=100)),
                ('domain', models.CharField(default='', max_length=100)),
                ('times_redirected', models.IntegerField(default=0)),
            ],
        ),
    ]
