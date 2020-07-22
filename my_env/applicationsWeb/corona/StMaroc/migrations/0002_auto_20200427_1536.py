# Generated by Django 3.0.5 on 2020-04-27 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('StMaroc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stmaroc',
            name='casesD',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='stmaroc',
            name='deathD',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='stmaroc',
            name='recovD',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='stmaroc',
            name='testsD',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='stmaroc',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 27, 15, 36, 28, 52251, tzinfo=utc)),
        ),
    ]
