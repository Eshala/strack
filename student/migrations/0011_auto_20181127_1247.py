# Generated by Django 2.1 on 2018-11-27 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20181127_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 27, 12, 47, 19, 699888)),
        ),
        migrations.AlterField(
            model_name='student',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 27, 12, 47, 19, 698230)),
        ),
    ]