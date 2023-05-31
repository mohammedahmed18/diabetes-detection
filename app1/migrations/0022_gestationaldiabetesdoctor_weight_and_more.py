# Generated by Django 4.2.1 on 2023-05-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0021_alter_diabetesdetectiondoctor_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="gestationaldiabetesdoctor",
            name="weight",
            field=models.FloatField(default=52),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gestationaldiabetespatient",
            name="weight",
            field=models.FloatField(default=25),
            preserve_default=False,
        ),
    ]
