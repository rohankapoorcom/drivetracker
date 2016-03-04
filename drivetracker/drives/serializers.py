from rest_framework import serializers

from drivetracker.drives.models import HardDrive


class HardDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardDrive
        fields = ('id', 'host', 'manufacturer', 'model', 'serial', 'capacity',
                  'capacity_unit', 'media_type', 'interface', 'form_factor',
                  'rpm', 'position', 'in_use', 'status', 'purchase_date',
                  'warranty_date', 'service_start_date', 'service_end_date',
                  'notes')
