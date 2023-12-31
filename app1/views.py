from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from itertools import chain


# Create your views here.




class DiabetesDetectionPatientView(generics.GenericAPIView):
    serializer_class = DiabetesDetectionPatientSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_patient:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                detection = serializer.save(patient=request.user.patient)
                detection.save()
                return Response(
                    "Saved Successfully",
                    status=status.HTTP_200_OK,
                )
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class DiabetesDetectionDoctorView(generics.GenericAPIView):
    serializer_class = DiabetesDetectionDoctorSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_doctor:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                detection = serializer.save(doctor=request.user.doctor)
                detection.save()
                return Response(
                    "Saved Successfully",
                    status=status.HTTP_200_OK,
                )
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class GestationalDiabetesPatientView(generics.GenericAPIView):
    serializer_class = GestationalDiabetesPatientSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_patient:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                detection = serializer.save(patient=request.user.patient)
                detection.save()
                return Response(
                   "Saved Successfully",
                    status=status.HTTP_200_OK,
                )
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class GestationalDiabetesDoctorView(generics.GenericAPIView):
    serializer_class = GestationalDiabetesDoctorSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_doctor:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                detection = serializer.save(doctor=request.user.doctor)
                detection.save()
                return Response(
                    "Saved Successfully",
                    status=status.HTTP_200_OK,
                )
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RetinopathyDetectionPatientView(generics.GenericAPIView):
    serializer_class = RetinopathyDetectionPatientSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_patient:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                detection = serializer.save(patient=request.user.patient)
                detection.save()
                return Response(
                    "Saved Successfully",
                    status=status.HTTP_200_OK,
                )
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RetinopathyDetectionDoctorView(generics.GenericAPIView):
    serializer_class = RetinopathyDetectionDoctorSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_doctor:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                detection = serializer.save(doctor=request.user.doctor)
                detection.save()
                return Response(
                    "Saved Successfully",
                    status=status.HTTP_200_OK,
                )
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

class PatientHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_patient:
                diabetes_detections = DiabetesDetectionPatient.objects.filter(
                    patient=request.user.patient
                )
                gestational_detections = GestationalDiabetesPatient.objects.filter(
                    patient=request.user.patient
                )
                retinopathy_detections = RetinopathyDetectionPatient.objects.filter(
                    patient=request.user.patient
                )
                detections_list = list(
                    chain(diabetes_detections, gestational_detections, retinopathy_detections)
                )
                ordered_detections = sorted(
                    detections_list, key=lambda x: x.date, reverse=True
                )
                serialized_detections = []
                for detection in ordered_detections:
                    if isinstance(detection, DiabetesDetectionPatient):
                        serialized_detection = DiabetesDetectionPatientSerializer(
                            detection
                        ).data
                    elif isinstance(detection, GestationalDiabetesPatient):
                        serialized_detection = GestationalDiabetesPatientSerializer(
                            detection
                        ).data
                    elif isinstance(detection, RetinopathyDetectionPatient):
                        serialized_detection = RetinopathyDetectionPatientSerializer(
                            detection
                        ).data
                    else:
                        continue
                    serialized_detections.append(serialized_detection)
                return Response(serialized_detections, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class DoctorHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_doctor:
                diabetes_detections = DiabetesDetectionDoctor.objects.filter(
                    doctor=request.user.doctor
                )
                gestational_detections = GestationalDiabetesDoctor.objects.filter(
                    doctor=request.user.doctor
                )
                retinopathy_detections = RetinopathyDetectionDoctor.objects.filter(
                    doctor=request.user.doctor
                )
                detections_list = list(
                    chain(diabetes_detections, gestational_detections, retinopathy_detections)
                )
                ordered_detections = sorted(
                    detections_list, key=lambda x: x.date, reverse=True
                )
                serialized_detections = []
                for detection in ordered_detections:
                    if isinstance(detection, DiabetesDetectionDoctor):
                        serialized_detection = DiabetesDetectionDoctorSerializer(
                            detection
                        ).data
                    elif isinstance(detection, GestationalDiabetesDoctor):
                        serialized_detection = GestationalDiabetesDoctorSerializer(
                            detection
                        ).data
                    elif isinstance(detection, RetinopathyDetectionDoctor):
                        serialized_detection = RetinopathyDetectionDoctorSerializer(
                            detection
                        ).data
                    else:
                        continue
                    serialized_detections.append(serialized_detection)
                return Response(serialized_detections, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
