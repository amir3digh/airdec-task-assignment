from django.urls import path
from .views import EstimateCreateView, EstimateDetailView, EstimateListView

urlpatterns = [
    path('create/', EstimateCreateView.as_view(), name='create-estimate'),
    path('list/', EstimateListView.as_view(), name='list-estimates'),
    path('detail/<int:pk>/', EstimateDetailView.as_view(), name='estimate-detail'),
]
