from rest_framework import serializers
from .models import *


# DiabetesDetection
class DiabetesDetectionPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabetesDetectionPatient
        fields = (
            "type",
            "date",
            "height",
            "phone",
            "weight",
            "age",
            "gender",
            "cholesterol",
            "glucose",
            "hdl_choll",
            "systolic_bp",
            "diastolic_bp",
            "result",
        )


class DiabetesDetectionDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabetesDetectionDoctor
        fields = (
            "type",
            "date",
            "patient_name",
            "height",
            "phone",
            "weight",
            "age",
            "gender",
            "cholesterol",
            "glucose",
            "hdl_choll",
            "systolic_bp",
            "diastolic_bp",
            "result",
        )


class GestationalDiabetesPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestationalDiabetesPatient
        fields = (
            "type",
            "date",
            "height",
            "weight",
            "phone",
            "number_of_pregnancies",
            "age",
            "bmi",
            "bp_level",
            "glucose",
            "insulin",
            "skin_thickness",
            "diabetes_pedigree",
            "result",
        )


class GestationalDiabetesDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestationalDiabetesDoctor
        fields = (
            "type",
            "date",
            "patient_name",
            "height",
            "weight",
            "phone",
            "number_of_pregnancies",
            "age",
            "bmi",
            "bp_level",
            "glucose",
            "insulin",
            "skin_thickness",
            "diabetes_pedigree",
            "result",
        )
