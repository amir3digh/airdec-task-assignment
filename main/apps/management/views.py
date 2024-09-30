from library import CustomListAPIView
from main.apps.management.models import Equipment
from main.apps.management.serializers import EquipmentListSerializer


# Custom api views make views more scalable and customizable. middlewares also can be used.
# For example making template responses can add more information to each request for frontend
class EquipmentListView(CustomListAPIView):
    # TODO: add pagination
    queryset = Equipment.objects.all()
    serializer_class = EquipmentListSerializer
