# Generated by Django 3.1.2 on 2023-05-23 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paitentprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='DoctorProfile',
        ),
        migrations.DeleteModel(
            name='PaitentProfile',
        ),
    ]
