from rest_framework import serializers

from main.apps.management.models import Equipment


class EquipmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            'id',
            'name',
            'price',
            'flag',
        ]
