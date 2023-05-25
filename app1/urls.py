from django.urls import path
from .views import PatientSignupView, DoctorSignupView, LoginView
from .views import PasswordReset,ResetPasswordAPI
from .views import DiabetesDetectionView,GestationalDiabetesView
from . import views


urlpatterns = [
    path('signup/patient/',  PatientSignupView.as_view()),
    path('signup/doctor/',  DoctorSignupView.as_view()),
    path('login/', LoginView.as_view()),
    # path('logout/', logout.as_view()),
    path(
        "request-password-reset/",
        views.PasswordReset.as_view(),
        name="request-password-reset",
    ),
    path(
        "password-reset/<str:encoded_pk>/<str:token>/",
        views.ResetPasswordAPI.as_view(),
        name="reset-password",
    ),

    path('DiabetesDetection/patient/',  DiabetesDetectionView.as_view()),
    path('GestationalDiabetes/patient', GestationalDiabetesView.as_view()),

]
