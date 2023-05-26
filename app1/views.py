from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import Patient, Doctor, User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework import views

# Create your views here.


class PatientSignupView(generics.GenericAPIView):
    serializer_class = PatientSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(username=request.data.get("username"))
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "phone": user.Patient.phone,
                # "user": user.username,
                # "token": token_obj.key,
                # "message": "account created successfully"
            }
        )


class DoctorSignupView(generics.GenericAPIView):
    serializer_class = DoctorSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(username=request.data.get("username"))
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                # "user": user.username,
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "phone": user.Doctor.phone,
                # "token": token_obj.key,
                # "message": "account created successfully"
            }
        )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)

            return Response(
                {
                    "token": token.key,
                }
            )
        else:
            return Response(
                {"errors": {"non_field_errors": ["Email or Password is not Valid"]}}
            )


from rest_framework import generics, status, viewsets, response

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model

User = get_user_model()

from . import serializers


class PasswordReset(generics.GenericAPIView):
    """
    Request for Password Reset Link.
    """

    serializer_class = serializers.EmailSerializer

    def post(self, request):
        """
        Create token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"localhost:8000{reset_url}"

            # send the rest_link as mail to the user.

            return response.Response(
                {"message": f"Your password rest link: {reset_link}"},
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = serializers.ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )


# =====================================Patient===================================================================
# DiabetesDetection
class DiabetesDetectionView(generics.GenericAPIView):
    serializer_class = DiabetesDetectionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "DiabetesDetection": DiabetesDetectionSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            }
        )


class GestationalDiabetesView(generics.GenericAPIView):
    serializer_class = GestationalDiabetesSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "Gestational Diabetes": GestationalDiabetesSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            }
        )
