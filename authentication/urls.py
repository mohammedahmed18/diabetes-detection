from django.urls import path
from .views import *

urlpatterns = [
    path("signup/patient/", PatientSignupView.as_view()),
    path("signup/doctor/", DoctorSignupView.as_view()),
    path("login/", LoginView.as_view()),
    # path('logout/', logout.as_view()),
    path(
        "request-password-reset/",
        PasswordReset.as_view(),
        name="request-password-reset",
    ),
    path(
        "password-reset/<str:encoded_pk>/<str:token>/",
        ResetPasswordAPI.as_view(),
        name="reset-password",
    ),
]