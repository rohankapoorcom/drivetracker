from django.test import TestCase
from drivetracker.drives.serializers import HardDriveSerializer
from drivetracker.drives import models


class HardDriveSeralizerTestCase(TestCase):
    """Unit tests for the HardDriveSerializer"""

    def test_serializing_empty_hard_drive(self):
        """Verify that an empty hard drive provides only the id"""
        hd = models.HardDrive()
        hd.save()
        expected_value = {
            'status': 'Unknown',
            'service_end_date': None,
            'position': '',
            'capacity': '',
            'in_use': 'Unknown',
            'notes': '',
            'warranty_date': None,
            'service_start_date': None,
            'host': None,
            'purchase_date': None,
            'form_factor': '',
            'interface': 'Unknown',
            'media_type': '',
            'model': None,
            'rpm': None,
            'id': 9523044409L,
            'serial': '',
            'manufacturer': None
        }
        expected_value.pop('id', None)
        actual_value = HardDriveSerializer(hd).data
        actual_value.pop('id', None)
        self.assertEqual(actual_value, expected_value)

    def test_serializing_with_host(self):
        raise NotImplementedError

    def test_serializing_with_manufacturer(self):
        raise NotImplementedError

    def test_serializing_with_model(self):
        raise NotImplementedError

    def test_serializing_with_capacity(self):
        raise NotImplementedError

    def test_serializing_with_in_use(self):
        raise NotImplementedError

    def test_serializing_with_status(self):
        raise NotImplementedError

    def test_serializing_with_interface(self):
        raise NotImplementedError

    def test_serializing_with_filled_hard_drive(self):
        raise NotImplementedError
