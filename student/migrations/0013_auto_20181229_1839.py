# Generated by Django 2.1 on 2018-12-29 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20181229_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='archive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pay',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 29, 18, 39, 22, 542648)),
        ),
        migrations.AlterField(
            model_name='student',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 29, 18, 39, 22, 540492)),
        ),
    ]