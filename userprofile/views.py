from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from app1.models import Patient, Doctor
from rest_framework.views import APIView

# Create your views here.


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = TokenAuthentication

    def get(self, request):
        try:
            if request.user.is_patient == True:
                user_profile = Patient.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                response = {
                    "success": "true",
                    "status code": status_code,
                    "message": "Paitent profile fetched successfully",
                    "data": [
                        {
                            "username": user_profile.username,
                            "email": user_profile.email,
                            "phone": user_profile.phone,
                        }
                    ],
                }
            if request.user.is_doctor == True:
                user_profile = Doctor.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                response = {
                    "success": "true",
                    "status code": status_code,
                    "message": "Doctor profile fetched successfully",
                    "data": [
                        {
                            "username": user_profile.username,
                            "email": user_profile.email,
                            "phone": user_profile.phone,
                        }
                    ],
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                "success": "false",
                "status code": status.HTTP_400_BAD_REQUEST,
                "message": "User does not exists",
                "error": str(e),
            }
        return Response(response, status=status_code)
