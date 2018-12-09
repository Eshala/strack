# Generated by Django 2.1 on 2018-12-09 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20181208_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='transaction_type',
            field=models.CharField(choices=[('C', 'Credit'), ('D', 'Debit')], default='D', max_length=2),
        ),
        migrations.AlterField(
            model_name='pay',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 18, 30, 5, 581072)),
        ),
        migrations.AlterField(
            model_name='student',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 9, 18, 30, 5, 579583)),
        ),
    ]
