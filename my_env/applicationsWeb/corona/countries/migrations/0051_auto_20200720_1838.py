# Generated by Django 3.0.5 on 2020-07-20 18:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0050_auto_20200720_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 18, 38, 22, 150359, tzinfo=utc)),
        ),
    ]