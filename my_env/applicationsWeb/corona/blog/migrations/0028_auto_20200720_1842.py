# Generated by Django 3.0.5 on 2020-07-20 18:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20200720_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 7, 20, 18, 41, 59, 921893, tzinfo=utc)),
        ),
    ]
