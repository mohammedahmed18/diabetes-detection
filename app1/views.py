from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.

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

class HistoryView(APIView):
    def get(self, request):
        if request.user.is_patient:
            pass
        else:
            pass