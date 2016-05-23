from rest_framework import serializers
from rest_framework.fields import ReadOnlyField, SerializerMethodField

from drivetracker.drives.models import HardDrive


class HardDriveSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField()
    manufacturer = serializers.StringRelatedField()
    model = serializers.StringRelatedField()
    capacity = SerializerMethodField('_get_capacity_representation')
    in_use = ReadOnlyField(source='get_in_use_representation')
    status = ReadOnlyField(source='get_status_representation')
    interface = ReadOnlyField(source='get_interface_representation')

    class Meta:
        model = HardDrive
        fields = ('id', 'host', 'manufacturer', 'model', 'serial', 'capacity',
                  'media_type', 'interface', 'form_factor', 'rpm', 'position',
                  'in_use', 'status', 'purchase_date', 'warranty_date',
                  'service_start_date', 'service_end_date', 'notes')

    def _get_capacity_representation(self, obj):
        if self.context.get('representation', None) == 'original':
            return obj.capacity
        return obj.get_capacity_representation()
