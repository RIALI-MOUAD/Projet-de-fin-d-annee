# Generated by Django 3.0.5 on 2020-04-27 15:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0029_auto_20200427_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 15, 25, 23, 200496, tzinfo=utc)),
        ),
    ]
