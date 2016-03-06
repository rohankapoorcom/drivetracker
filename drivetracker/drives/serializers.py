from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from drivetracker.drives.models import HardDrive


class HardDriveSerializer(serializers.ModelSerializer):
    capacity = SerializerMethodField('_get_capacity_representation')
    in_use = SerializerMethodField('_get_in_use_representation')

    class Meta:
        model = HardDrive
        fields = ('id', 'host', 'manufacturer', 'model', 'serial', 'capacity',
                  'media_type', 'interface', 'form_factor', 'rpm', 'position',
                  'in_use', 'status', 'purchase_date', 'warranty_date',
                  'service_start_date', 'service_end_date', 'notes')

    def _get_capacity_representation(self, obj):
        if self.context['representation'] == 'original':
            return obj.capacity
        return obj.get_capacity_representation()

    def _get_in_use_representation(self, obj):
        if self.context['representation'] == 'original':
            return obj.in_use
        return obj.get_in_use_representation()
