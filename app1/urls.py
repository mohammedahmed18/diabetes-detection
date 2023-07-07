from django.urls import path
from .views import *


urlpatterns = [
    path("diabetes-detection/patient/", DiabetesDetectionPatientView.as_view()),
    path("gestational-diabetes/patient/", GestationalDiabetesPatientView.as_view()),
    path("retinopathy-detection/patient/", RetinopathyDetectionPatientView.as_view()),
    path("diabetes-detection/doctor/", DiabetesDetectionDoctorView.as_view()),
    path("gestational-diabetes/doctor/", GestationalDiabetesDoctorView.as_view()),
    path("retinopathy-detection/doctor/", RetinopathyDetectionDoctorView.as_view()),
    path("history/patient/", PatientHistoryView.as_view()),
    path("history/doctor/", DoctorHistoryView.as_view()),
]
