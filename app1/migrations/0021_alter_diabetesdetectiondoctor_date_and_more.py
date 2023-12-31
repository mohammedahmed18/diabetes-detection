# Generated by Django 4.2.1 on 2023-05-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0020_alter_diabetesdetectiondoctor_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diabetesdetectiondoctor",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="diabetesdetectionpatient",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="gestationaldiabetesdoctor",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="gestationaldiabetespatient",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
