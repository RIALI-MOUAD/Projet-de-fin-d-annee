# Generated by Django 3.0.5 on 2020-04-30 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200430_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 30, 17, 43, 10, 746427, tzinfo=utc)),
        ),
    ]
