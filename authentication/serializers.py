from rest_framework import serializers
from app1.models import User
from app1.models import Patient, Doctor
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class PatientSignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Patient
        fields = ("username", "email", "password", "phone")

    def create(self, validated_data):
        username = validated_data.pop("username")
        email = validated_data["email"]
        password = validated_data.pop("password")
        user = User(username=username, email=email, is_patient=True)
        user.set_password(password)
        user.save()

        validated_data["user"] = user
        validated_data["name"] = user.username
        patient = super(PatientSignupSerializer, self).create(validated_data)
        return patient


class DoctorSignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Doctor
        fields = ("username", "email", "password", "phone")

    def create(self, validated_data):
        username = validated_data.pop("username")
        email = validated_data["email"]
        password = validated_data.pop("password")
        user = User(username=username, email=email, is_doctor=True)
        user.set_password(password)
        user.save()
        validated_data["user"] = user
        validated_data["name"] = user.username
        doctor = super(DoctorSignupSerializer, self).create(validated_data)
        return doctor


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            if not user:
                msg = "Access denied: wrong username or password."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs


class EmailSerializer(serializers.Serializer):
    """
    Reset Password Email Request Serializer.
    """

    email = serializers.EmailField()

    class Meta:
        fields = ("email",)


class ResetPasswordSerializer(serializers.Serializer):
    """
    Reset Password Serializer.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = "password"

    def validate(self, data):
        """
        Verify token and encoded_pk and then set new password.
        """
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data
