from rest_framework import serializers
from .models import  DiabetesDetection, GestationalDiabetes

# DiabetesDetection
class DiabetesDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabetesDetection
        fields = (
            "age",
            "gender",
            "cholesterol",
            "glucose",
            "hdl_choll",
            "systolic_bp",
            "diastolic_bp",
        )


class GestationalDiabetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestationalDiabetes
        fields = (
            "number_of_pregnancies",
            "age",
            "bmi",
            "bp_level",
            "glucose",
            "insulin",
            "skin_thickness",
            "diabetes_pedigree",
        )

