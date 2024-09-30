from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from library import CustomListAPIView
from .models import Estimate
from .serializers import EstimateSerializer
from main.apps.user.permissions import IsAdminUserOrReadOnly


class EstimateCreateView(generics.CreateAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [IsAdminUser]


class EstimateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [IsAdminUserOrReadOnly]


# list of estimates added for frontend to manage estimates and do partial updated
class EstimateListView(CustomListAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
