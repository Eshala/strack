# Generated by Django 2.1 on 2018-12-07 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20181207_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 16, 40, 13, 721132)),
        ),
        migrations.AlterField(
            model_name='student',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 7, 16, 40, 13, 719517)),
        ),
    ]