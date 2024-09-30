import rest_framework.request
from rest_framework import serializers
from .models import Estimate, EstimateEquipment


class EstimateEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstimateEquipment
        fields = ['id', 'equipment', 'quantity', 'price_override', 'created_at']
        read_only_fields = ['id', 'created_at']


class EstimateSerializer(serializers.ModelSerializer):
    equipments = EstimateEquipmentSerializer(many=True, required=False)
    equipments_list = EstimateEquipmentSerializer(
        source='estimateequipment_set',
        many=True,
        required=False,
        read_only=True,
    )

    class Meta:
        model = Estimate
        fields = ['id', 'note', 'created_at', 'created_by', 'archive', 'equipments', 'equipments_list']
        read_only_fields = ['created_at', 'created_by']

    def create(self, validated_data):
        request: rest_framework.request.Request = self.context.get('request')
        equipments_data = validated_data.pop('equipments', [])

        # Automatically detect user from authenticated request
        estimate = Estimate.objects.create(created_by=request.user, **validated_data)

        for equipment_data in equipments_data:
            EstimateEquipment.objects.create(estimate=estimate, **equipment_data)

        return estimate

    def update(self, instance, validated_data):
        equipments_data = validated_data.pop('equipments', [])

        # Update the Estimate object
        instance.note = validated_data.get('note', instance.note)
        instance.archive = validated_data.get('archive', instance.archive)
        instance.save()

        # this is not optimized for large list of estimate equipment.
        # TODO: Adding endpoints for each estimate equipment can improve performance
        instance.estimateequipment_set.all().delete()
        for equipment_data in equipments_data:
            EstimateEquipment.objects.create(estimate=instance, **equipment_data)

        return instance
