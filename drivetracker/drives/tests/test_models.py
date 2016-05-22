from django.test import TestCase
from django.db import IntegrityError
import drivetracker.drives.models as models


class HostTestCase(TestCase):
    """Unit tests for the Host class"""

    def test_string_representation(self):
        """Verify that the string representation is readable"""
        host_name = 'ORACLE'
        host = models.Host(name=host_name)
        self.assertEqual(str(host), host_name)

    def test_host_names_are_unique(self):
        """Verify that Host objects cannot have duplicate names"""
        host_name = 'ORACLE'
        host_a = models.Host(name=host_name)
        host_a.save()
        with self.assertRaises(IntegrityError):
            host_b = models.Host(name=host_name)
            host_b.save()


class ManufacturerTestCase(TestCase):
    """Unit tests for the Manufacturer class"""

    def test_string_representation(self):
        """Verify that the string representation is readable"""
        manufacturer_name = 'Seagate'
        manufacturer = models.Manufacturer(name=manufacturer_name)
        self.assertEqual(str(manufacturer), manufacturer_name)

    def test_manufacturer_names_are_unique(self):
        """Verify that Manufacturer objects cannot have duplicate names"""
        manufacturer_name = 'Seagate'
        manufacturer_a = models.Manufacturer(name=manufacturer_name)
        manufacturer_a.save()
        with self.assertRaises(IntegrityError):
            manufacturer_b = models.Manufacturer(name=manufacturer_name)
            manufacturer_b.save()


class ModelTestCase(TestCase):
    """Unit tests for the Model class"""

    def test_string_representation(self):
        """Verify that the string representation is readable"""
        model_name = 'STA30001D'
        model = models.Model(name=model_name)
        self.assertEqual(str(model), model_name)

    def test_model_names_are_unique(self):
        """Verify that Model objects cannot have duplicate names"""
        model_name = 'STA30001D'
        model_a = models.Model(name=model_name)
        model_a.save()
        with self.assertRaises(IntegrityError):
            model_b = models.Model(name=model_name)
            model_b.save()


class HardDriveTestCase(TestCase):
    """Unit tests for the HardDrive class"""

    def test_hard_drive_id_numbers_unique(self):
        """
        Verify that two HardDrive objects are not created with the same ID
        """
        hd_1 = models.HardDrive()
        hd_1.save()
        hd_2 = models.HardDrive()
        hd_2.save()
        self.assertNotEqual(hd_1.id, hd_2.id)

    def test_hard_drive_with_no_details(self):
        """
        Verify that a HardDrive object can be created with no information
        provided
        """
        hd = models.HardDrive()
        hd.save()

    def test_hard_drive_host_foreignkey_nullable(self):
        """
        Verify that a HardDrive object can have a null link to Host object
        """
        hd = models.HardDrive()
        hd.save()
        self.assertEqual(hd.host, None)

    def test_hard_drive_host_foreignkey_settable(self):
        """Verify that a HardDrive object can be linked to a Host object"""
        host = models.Host(name='Test Host')
        host.save()
        hd = models.HardDrive()
        hd.host = host
        hd.save()
        hd_id = hd.id
        # reload from db to make sure the object has changed
        hd = models.HardDrive.objects.get(id=hd_id)
        self.assertEqual(hd.host, host)

    def test_hard_drive_host_delete_foreignkey(self):
        """
        Verify that a HardDrive object will not be deleted when the linked Host
        object is deleted
        """
        host = models.Host(name='Test Host')
        host.save()
        hd = models.HardDrive(host=host)
        hd.save()
        hd_id = hd.id
        host.delete()
        # reload from db to make sure the object has changed
        hd = models.HardDrive.objects.get(id=hd_id)
        self.assertEqual(hd.host, None)

    def test_hard_drive_manufacturer_foreignkey_nullable(self):
        """
        Verify that a HardDrive object can have a null link to a Manufacturer
        object
        """
        hd = models.HardDrive()
        hd.save()
        self.assertEqual(hd.manufacturer, None)

    def test_hard_drive_manufacturer_foreignkey_settable(self):
        """
        Verify that a HardDrive object can be linked to a Manufacturer object
        """
        manufacturer = models.Manufacturer(name='Test Manufacturer')
        manufacturer.save()
        hd = models.HardDrive()
        hd.manufacturer = manufacturer
        hd.save()
        hd_id = hd.id
        # reload from db to make sure the object has changed
        hd = models.HardDrive.objects.get(id=hd_id)
        self.assertEqual(hd.manufacturer, manufacturer)

    def test_hard_drive_manufacturer_delete_foreignkey(self):
        """
        Verify that a HardDrive object will not be deleted when the linked
        Manufacturer object is deleted
        """
        manufacturer = models.Manufacturer(name='Test Manufacturer')
        manufacturer.save()
        hd = models.HardDrive()
        hd.manufacturer = manufacturer
        hd.save()
        hd_id = hd.id
        manufacturer.delete()
        # reload from db to make the object has change
        hd = models.HardDrive.objects.get(id=hd_id)
        self.assertEqual(hd.manufacturer, None)

    def test_hard_drive_model_foreignkey_nullable(self):
        """
        Verify that a HardDrive object can have a null link to a Model
        object
        """
        hd = models.HardDrive()
        hd.save()
        self.assertEqual(hd.model, None)

    def test_hard_drive_model_foreignkey_settable(self):
        """
        Verify that a HardDrive object can be linked to a Model object
        """
        model = models.Model(name='Test Model')
        model.save()
        hd = models.HardDrive()
        hd.model = model
        hd.save()
        hd_id = hd.id
        # reload from db to make sure the object has changed
        hd = models.HardDrive.objects.get(id=hd_id)
        self.assertEqual(hd.model, model)

    def test_hard_drive_model_delete_foreignkey(self):
        """
        Verify that a HardDrive object will not be deleted when the linked
        Model object is deleted
        """
        model = models.Model(name='Test model')
        model.save()
        hd = models.HardDrive()
        hd.model = model
        hd.save()
        hd_id = hd.id
        model.delete()
        # reload from db to make the object has change
        hd = models.HardDrive.objects.get(id=hd_id)
        self.assertEqual(hd.model, None)
