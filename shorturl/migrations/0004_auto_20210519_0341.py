# Generated by Django 3.0.5 on 2021-05-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0003_auto_20210519_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='expire_at',
            field=models.IntegerField(default=1621395975978),
        ),
    ]
