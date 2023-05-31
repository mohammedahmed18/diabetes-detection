# Generated by Django 4.2.1 on 2023-05-30 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0009_rename_age43_diabetesdetection_age"),
    ]

    operations = [
        migrations.RenameField(
            model_name="doctor",
            old_name="Doctor_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="patient",
            old_name="patient_name",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="patients",
        ),
        migrations.AddField(
            model_name="patient",
            name="doctor",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="app1.doctor"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="doctor",
            name="gender",
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
