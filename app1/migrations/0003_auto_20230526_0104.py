# Generated by Django 3.1.2 on 2023-05-25 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20230525_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diabetesdetection',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='diabetesdetection',
            name='Hight',
        ),
        migrations.RemoveField(
            model_name='diabetesdetection',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='gestationaldiabetes',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='gestationaldiabetes',
            name='Hight',
        ),
        migrations.RemoveField(
            model_name='gestationaldiabetes',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='gestationaldiabetes',
            name='Weight',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
    ]
