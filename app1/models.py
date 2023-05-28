from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, related_name="Patient", on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=150)
    age = models.IntegerField(null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=50)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def _str_(self) -> str:
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, related_name="Doctor", on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    Doctor_name = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=50)
    patients = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    def _str_(self) -> str:
        return self.user.username


# ============================================ Patient===========================================
# DiabetesDetection
class DiabetesDetection(models.Model):
    weight = models.FloatField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    cholesterol = models.FloatField()
    glucose = models.FloatField()
    hdl_choll = models.FloatField()
    systolic_bp = models.FloatField()
    diastolic_bp = models.FloatField()

    def _str_(self) -> str:
        return self.Weight


class GestationalDiabetes(models.Model):
    number_of_pregnancies = models.IntegerField()
    age = models.IntegerField()
    bmi = models.FloatField()
    bp_level = models.FloatField()
    glucose = models.FloatField()
    insulin = models.FloatField()
    skin_thickness = models.FloatField()
    diabetes_pedigree = models.FloatField()

    def _str_(self) -> str:
        return self.number_of_pregnancies
