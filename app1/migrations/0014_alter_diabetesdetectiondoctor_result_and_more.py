# Generated by Django 4.2.1 on 2023-05-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0013_diabetesdetectiondoctor_diabetesdetectionpatient_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diabetesdetectiondoctor",
            name="result",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="diabetesdetectionpatient",
            name="result",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="gestationaldiabetesdoctor",
            name="result",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="gestationaldiabetespatient",
            name="result",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
