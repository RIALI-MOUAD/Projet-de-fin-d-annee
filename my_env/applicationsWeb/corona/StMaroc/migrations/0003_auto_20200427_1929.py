# Generated by Django 3.0.5 on 2020-04-27 19:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('StMaroc', '0002_auto_20200427_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stmaroc',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 27, 19, 29, 29, 384423, tzinfo=utc)),
        ),
    ]
