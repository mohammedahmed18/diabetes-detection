import pytz
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, related_name="patient", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    age = models.IntegerField(null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=6)

    def _str_(self) -> str:
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, related_name="doctor", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=6)

    def _str_(self) -> str:
        return self.user.username


class DiabetesDetection(models.Model):
    type = models.CharField(default="Diabetes Detection", max_length=150, null=True)
    weight = models.FloatField()
    height = models.FloatField()
    phone = models.FloatField()
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    cholesterol = models.FloatField()
    glucose = models.FloatField()
    hdl_choll = models.FloatField()
    systolic_bp = models.FloatField()
    diastolic_bp = models.FloatField()
    result = models.CharField(null=True, blank=True, max_length=100)
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def _str_(self) -> str:
        return self.Weight

    class Meta:
        abstract = True


class DiabetesDetectionPatient(DiabetesDetection):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class DiabetesDetectionDoctor(DiabetesDetection):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=150)


class GestationalDiabetes(models.Model):
    type = models.CharField(
        default="Gestational Diabetes Detection", max_length=150, null=True
    )
    number_of_pregnancies = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    phone = models.FloatField()
    age = models.IntegerField()
    bmi = models.FloatField()
    bp_level = models.FloatField()
    glucose = models.FloatField()
    insulin = models.FloatField()
    skin_thickness = models.FloatField()
    diabetes_pedigree = models.FloatField()
    result = models.CharField(null=True, blank=True, max_length=100)
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def _str_(self) -> str:
        return self.Weight

    class Meta:
        abstract = True


class GestationalDiabetesPatient(GestationalDiabetes):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class GestationalDiabetesDoctor(GestationalDiabetes):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=150)
