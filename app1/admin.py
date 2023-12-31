from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(DiabetesDetectionPatient)
admin.site.register(GestationalDiabetesPatient)
admin.site.register(RetinopathyDetectionPatient)
admin.site.register(DiabetesDetectionDoctor)
admin.site.register(GestationalDiabetesDoctor)
admin.site.register(RetinopathyDetectionDoctor)
