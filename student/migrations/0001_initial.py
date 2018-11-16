# Generated by Django 2.1.dev20180313180640 on 2018-09-27 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('group', '0003_auto_20180926_1951'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('phone_number', models.IntegerField(blank=True)),
                ('fee_submitted', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Shift')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
