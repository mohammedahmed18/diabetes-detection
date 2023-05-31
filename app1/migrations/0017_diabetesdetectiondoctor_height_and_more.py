# Generated by Django 4.2.1 on 2023-05-31 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0016_diabetesdetectiondoctor_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="diabetesdetectiondoctor",
            name="height",
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="diabetesdetectiondoctor",
            name="phone",
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gestationaldiabetesdoctor",
            name="height",
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gestationaldiabetesdoctor",
            name="phone",
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="diabetesdetectiondoctor",
            name="gender",
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name="diabetesdetectionpatient",
            name="gender",
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name="patient",
            name="gender",
            field=models.CharField(max_length=6),
        ),
    ]