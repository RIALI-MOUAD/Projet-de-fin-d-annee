# Generated by Django 3.0.5 on 2020-04-26 11:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0006_auto_20200424_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 11, 25, 54, 404122, tzinfo=utc)),
        ),
    ]
