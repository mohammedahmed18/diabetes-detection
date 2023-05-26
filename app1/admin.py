from django.contrib import admin
from .models import User, Patient, Doctor, DiabetesDetection, GestationalDiabetes

# Register your models here.

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(DiabetesDetection)
admin.site.register(GestationalDiabetes)
