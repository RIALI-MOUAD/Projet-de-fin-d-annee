# Generated by Django 3.0.5 on 2020-07-17 12:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0037_auto_20200430_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 12, 55, 35, 712105, tzinfo=utc)),
        ),
    ]
