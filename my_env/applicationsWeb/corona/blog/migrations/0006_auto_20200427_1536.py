# Generated by Django 3.0.5 on 2020-04-27 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200427_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 27, 15, 36, 28, 51396, tzinfo=utc)),
        ),
    ]
