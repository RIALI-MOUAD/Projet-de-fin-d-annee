# Generated by Django 3.0.5 on 2020-07-17 12:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200717_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 7, 17, 12, 56, 54, 983693, tzinfo=utc)),
        ),
    ]
