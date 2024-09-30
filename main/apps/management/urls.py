from django.urls import path

from main.apps.management.views import EquipmentListView

# from .views import EstimateCreateView, EstimateDetailView

urlpatterns = [
    path('equipment/list/', EquipmentListView.as_view(), name='list')
]
