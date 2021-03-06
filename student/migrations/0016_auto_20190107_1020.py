# Generated by Django 2.1 on 2019-01-07 10:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20181229_1703'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0015_auto_20190106_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('phone_number', models.IntegerField(null=True)),
                ('joined_date', models.DateField(default=datetime.datetime(2019, 1, 7, 10, 20, 37, 502108))),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('intrested_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='pay',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 7, 10, 20, 37, 504202)),
        ),
        migrations.AlterField(
            model_name='student',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 7, 10, 20, 37, 501365)),
        ),
    ]
