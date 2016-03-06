from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from drivetracker.drives.models import HardDrive


class HardDriveSerializer(serializers.ModelSerializer):
    capacity = ReadOnlyField(source='get_capacity_representation')

    class Meta:
        model = HardDrive
        fields = ('id', 'host', 'manufacturer', 'model', 'serial', 'capacity',
                  'media_type', 'interface', 'form_factor', 'rpm', 'position',
                  'in_use', 'status', 'purchase_date', 'warranty_date',
                  'service_start_date', 'service_end_date', 'notes')
