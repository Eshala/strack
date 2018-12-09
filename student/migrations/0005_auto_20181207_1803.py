# Generated by Django 2.1 on 2018-12-07 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20181207_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupcourse',
            name='shift',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='groupcourse',
            name='course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='groupcourse',
            name='group',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pay',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 18, 3, 0, 672836)),
        ),
        migrations.AlterField(
            model_name='student',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 7, 18, 3, 0, 670953)),
        ),
    ]