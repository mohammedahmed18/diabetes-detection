from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from app1.models import Patient, Doctor
from rest_framework.views import APIView
from app1.serializers import PatientSerializer, DoctorSerializer

# Create your views here.


# class UserProfileView(APIView):
#     permission_classes = (IsAuthenticated,)
#     authentication_class = TokenAuthentication

#     def get(self, request):
#         try:
#             if request.user.is_patient == True:
#                 user_profile =Patient.objects.get(user=request.user)
#                 user=User.objects.get(id=request.user.id)
#                 status_code = status.HTTP_200_OK
#                 response = {
#                     # "success": "true",
#                     # "status code": status_code,
#                     # "message": "Paitent profile fetched successfully",
#                     "data": [
#                         {
#                             "username":user.username,
#                             "email": user_profile.email,
#                             "phone": user_profile.phone,
#                         }
#                     ],
#                 }
#             if request.user.is_doctor == True:
#                 user_profile = Doctor.objects.get(user=request.user)
#                 user=User.objects.get(id=request.user.id)
#                 status_code = status.HTTP_200_OK
#                 response = {
#                     # "success": "true",
#                     # "status code": status_code,
#                     # "message": "Doctor profile fetched successfully",
#                     "data": [
#                         {
#                             "username": user.username,
#                             "email": user_profile.email,
#                             "phone": user_profile.phone,
#                         }
#                     ],
#                 }

#         except Exception as e:
#             status_code = status.HTTP_400_BAD_REQUEST
#             response = {
#                 "success": "false",
#                 "status code": status.HTTP_400_BAD_REQUEST,
#                 "message": "User does not exists",
#                 "error": str(e),
#             }
#         return Response(response, status=status_code)

class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = TokenAuthentication

    def get(self, request):
        try:
            if request.user.is_patient:
                patient_profile = Patient.objects.get(user=request.user)
                serializer = PatientSerializer(patient_profile)
                status_code = status.HTTP_200_OK
                response = {
                    # "success": True,
                    # "status code": status_code,
                    # "message": "Patient profile fetched successfully",
                    "data": [serializer.data],
                }
            elif request.user.is_doctor:
                doctor_profile = Doctor.objects.get(user=request.user)
                serializer = DoctorSerializer(doctor_profile)
                status_code = status.HTTP_200_OK
                response = {
                    # "success": True,
                    # "status code": status_code,
                    # "message": "Doctor profile fetched successfully",
                    "data": [serializer.data],
                }
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                    "success": False,
                    "status code": status.HTTP_400_BAD_REQUEST,
                    "message": "User does not exist",
                }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                "success": False,
                "status code": status.HTTP_400_BAD_REQUEST,
                "message": "User does not exist",
                "error": str(e),
            }
        return Response(response, status=status_code)

    def put(self, request):
        try:
            if request.user.is_patient:
                patient_profile = Patient.objects.get(user=request.user)
                serializer = PatientSerializer(patient_profile, data=request.data)
            elif request.user.is_doctor:
                doctor_profile = Doctor.objects.get(user=request.user)
                serializer = DoctorSerializer(doctor_profile, data=request.data)
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                    "success": False,
                    "status code": status.HTTP_400_BAD_REQUEST,
                    "message": "User does not exist",
                }
                return Response(response, status=status_code)

            if serializer.is_valid():
                serializer.save()
                status_code = status.HTTP_200_OK
                response = {
                    "success": True,
                    "status code": status_code,
                    "message": "Profile updated successfully",
                    "data": [serializer.data],
                }
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                    "success": False,
                    "status code": status.HTTP_400_BAD_REQUEST,
                    "message": "Invalid data",
                    "errors": serializer.errors,
                }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                "success": False,
                "status code": status.HTTP_400_BAD_REQUEST,
                "message": "User does not exist",
                "error": str(e),
            }
        return Response(response, status=status_code)
