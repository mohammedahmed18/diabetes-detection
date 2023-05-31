# Generated by Django 4.2.1 on 2023-05-31 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0012_remove_patient_doctor"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiabetesDetectionDoctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.FloatField()),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=50)),
                ("cholesterol", models.FloatField()),
                ("glucose", models.FloatField()),
                ("hdl_choll", models.FloatField()),
                ("systolic_bp", models.FloatField()),
                ("diastolic_bp", models.FloatField()),
                ("result", models.FloatField()),
                ("patient_name", models.CharField(max_length=150)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DiabetesDetectionPatient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.FloatField()),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=50)),
                ("cholesterol", models.FloatField()),
                ("glucose", models.FloatField()),
                ("hdl_choll", models.FloatField()),
                ("systolic_bp", models.FloatField()),
                ("diastolic_bp", models.FloatField()),
                ("result", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GestationalDiabetesDoctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_pregnancies", models.IntegerField()),
                ("age", models.IntegerField()),
                ("bmi", models.FloatField()),
                ("bp_level", models.FloatField()),
                ("glucose", models.FloatField()),
                ("insulin", models.FloatField()),
                ("skin_thickness", models.FloatField()),
                ("diabetes_pedigree", models.FloatField()),
                ("result", models.FloatField()),
                ("patient_name", models.CharField(max_length=150)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GestationalDiabetesPatient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_pregnancies", models.IntegerField()),
                ("age", models.IntegerField()),
                ("bmi", models.FloatField()),
                ("bp_level", models.FloatField()),
                ("glucose", models.FloatField()),
                ("insulin", models.FloatField()),
                ("skin_thickness", models.FloatField()),
                ("diabetes_pedigree", models.FloatField()),
                ("result", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="DiabetesDetection",
        ),
        migrations.DeleteModel(
            name="GestationalDiabetes",
        ),
        migrations.AlterField(
            model_name="doctor",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="doctor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patient",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="gestationaldiabetespatient",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.patient"
            ),
        ),
        migrations.AddField(
            model_name="gestationaldiabetesdoctor",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.doctor"
            ),
        ),
        migrations.AddField(
            model_name="diabetesdetectionpatient",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.patient"
            ),
        ),
        migrations.AddField(
            model_name="diabetesdetectiondoctor",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.doctor"
            ),
        ),
    ]