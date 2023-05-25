from django.db import models


from django.db import models

from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token
# Create your models here.


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)




class Patient(models.Model):
    user = models.OneToOneField(
        User, related_name="Patient", on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=150)
    age = models.IntegerField(null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=50)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def _str_(self) -> str:
        return self.user.username




class Doctor(models.Model):
    user = models.OneToOneField(
        User, related_name="Doctor", on_delete=models.CASCADE)
    id= models.IntegerField(primary_key=True)   
    Doctor_name = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=50)
    patients = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)

    def _str_(self) -> str:
        return self.user.username





#============================================ Patient===========================================
#DiabetesDetection
class DiabetesDetection(models.Model):
    Weight=models.FloatField()
    Age=models.IntegerField()
    Gender=models.CharField(max_length=50)
    Cholesterol=models.FloatField()
    Glucose=models.FloatField()
    Hdl_CholL=models.FloatField()
    Systolic_BP=models.FloatField()
    Diastolic_BP=models.FloatField()

    def _str_(self) -> str:
        return self. Weight



class GestationalDiabetes(models.Model):
    Number_Of_Pregnancies=models.IntegerField()
    Age=models.IntegerField()
    Bmi=models.FloatField()
    BP_level=models.FloatField()
    Glucose=models.FloatField()
    Insulin=models.FloatField()
    Skin_Thickness=models.FloatField()
    Diabetes_Pedigree=models.FloatField()

    def _str_(self) -> str:
        return self.Number_Of_Pregnancies





