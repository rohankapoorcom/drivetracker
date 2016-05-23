from django.test import TestCase

from drivetracker.drives import models
from drivetracker.drives.serializers import HardDriveSerializer


class HardDriveSeralizerTestCase(TestCase):
    """Unit tests for the HardDriveSerializer"""

    def test_serializing_empty_hard_drive(self):
        """Verify that an empty HardDrive provides only the id"""
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
        """Verify that a HardDrive attached to a Host shows the Host's name"""
        host = models.Host(name='Test Host')
        host.save()
        hd = models.HardDrive(host=host)
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
            'host': 'Test Host',
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

    def test_serializing_with_manufacturer(self):
        """
        Verify that a HardDrive attached to a Manufacturer shows the
        Manufacturer's name
        """
        manufacturer = models.Manufacturer(name='Test Manufacturer')
        manufacturer.save()
        hd = models.HardDrive(manufacturer=manufacturer)
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
            'manufacturer': 'Test Manufacturer'
        }
        expected_value.pop('id', None)
        actual_value = HardDriveSerializer(hd).data
        actual_value.pop('id', None)
        self.assertEqual(actual_value, expected_value)

    def test_serializing_with_model(self):
        """
        Verify that a HardDrive attached to a Model shows the Model's name
        """
        model = models.Model(name='Test Model')
        model.save()
        hd = models.HardDrive()
        hd.model = model
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
            'model': 'Test Model',
            'rpm': None,
            'id': 9523044409L,
            'serial': '',
            'manufacturer': None
        }
        expected_value.pop('id', None)
        actual_value = HardDriveSerializer(hd).data
        actual_value.pop('id', None)
        self.assertEqual(actual_value, expected_value)

    def test_serializing_with_capacity(self):
        """
        Verify that a HardDrive with a capacity shows the capacity correctly
        """
        hd = models.HardDrive(capacity=120000000000)
        hd.save()
        expected_value = {
            'status': 'Unknown',
            'service_end_date': None,
            'position': '',
            'capacity': '120.0 GB',
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

    def test_serializing_with_in_use(self):
        """
        Verify that a HardDrive with the in_use flag set displays it correctly
        """
        hd = models.HardDrive(in_use=True)
        hd.save()
        expected_value = {
            'status': 'Unknown',
            'service_end_date': None,
            'position': '',
            'capacity': '',
            'in_use': 'Yes',
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

    def test_serializing_with_status(self):
        """
        Verify that a HardDrive with the status flag set displays it correctly
        """
        hd = models.HardDrive(status=True)
        hd.save()
        expected_value = {
            'status': 'Good',
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

    def test_serializing_with_interface(self):
        """
        Verify that a HardDrive with an interface set displays it correctly
        """
        hd = models.HardDrive(interface='SAS')
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
            'interface': 'SAS',
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

    def test_serializing_with_filled_hard_drive(self):
        """
        Verify that a HardDrive with many fields filled displays them all
        """
        host = models.Host(name='Test Host')
        host.save()
        manufacturer = models.Manufacturer(name='Test Manufacturer')
        manufacturer.save()
        model = models.Model(name='Test Model')
        model.save()
        hd = models.HardDrive(host=host, manufacturer=manufacturer,
                              model=model, serial='123456789',
                              capacity=120000000000, media_type='SSD',
                              interface='SAS', form_factor='2.5',
                              rpm=10000, position='3', in_use=True,
                              status=True)
        hd.save()
        expected_value = {
            'status': 'Good',
            'service_end_date': None,
            'position': '3',
            'capacity': '120.0 GB',
            'in_use': 'Yes',
            'notes': '',
            'warranty_date': None,
            'service_start_date': None,
            'host': 'Test Host',
            'purchase_date': None,
            'form_factor': '2.5',
            'interface': 'SAS',
            'media_type': 'SSD',
            'model': 'Test Model',
            'rpm': 10000,
            'id': 9523044409L,
            'serial': '123456789',
            'manufacturer': 'Test Manufacturer'
        }
        expected_value.pop('id', None)
        actual_value = HardDriveSerializer(hd).data
        actual_value.pop('id', None)
        self.assertEqual(actual_value, expected_value)
