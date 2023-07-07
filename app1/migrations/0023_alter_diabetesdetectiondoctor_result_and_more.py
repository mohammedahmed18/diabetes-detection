# Generated by Django 4.2.1 on 2023-07-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0022_gestationaldiabetesdoctor_weight_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diabetesdetectiondoctor",
            name="result",
            field=models.CharField(default="diabetic", max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="diabetesdetectionpatient",
            name="result",
            field=models.CharField(default="diabetic", max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="gestationaldiabetesdoctor",
            name="result",
            field=models.CharField(default="diabetic", max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="gestationaldiabetespatient",
            name="result",
            field=models.CharField(default="diabetic", max_length=150),
            preserve_default=False,
        ),
    ]
