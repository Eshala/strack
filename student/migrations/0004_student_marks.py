# Generated by Django 2.1 on 2018-11-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3),
        ),
    ]
