# Generated by Django 3.0.5 on 2020-07-19 09:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200717_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 7, 19, 9, 27, 2, 827740, tzinfo=utc)),
        ),
    ]
