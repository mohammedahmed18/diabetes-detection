from django.urls import path
from .views import *


urlpatterns = [
    path("diabetes-detection/patient/", DiabetesDetectionView.as_view()),
    path("gestational-diabetes/patient/", GestationalDiabetesView.as_view()),
]
