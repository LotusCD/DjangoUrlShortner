# Generated by Django 3.0.5 on 2021-05-16 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='expire_at',
            field=models.IntegerField(default=1621126221652),
        ),
    ]
