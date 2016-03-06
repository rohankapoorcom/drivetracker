from __future__ import unicode_literals

from django.db import models

from random import randint
import bitmath


def generate_id():
    """Generates a unique 10 digit identifier"""
    candidate = randint(1000000000, 9999999999)
    while HardDrive.objects.filter(id=candidate).count() > 0:
        candidate = randint(1000000000, 9999999999)
    return candidate


class HardDrive(models.Model):
    """
    Represents a hard drive and stores all types of relevant information
    about said hard drive.
    """
    HDD = 'HDD'
    SSD = 'SSD'
    SSHD = 'SSHD'
    MEDIA_TYPE_CHOICES = (
        (HDD, 'HDD'),
        (SSD, 'SSD'),
        (SSHD, 'SSHD'),

    )
    IDE = 'IDE'
    SATA = 'SATA'
    SAS = 'SAS'
    USB = 'USB'
    FIREWIRE = 'FW'
    THUNDERBOLT = 'TB'
    PCI_EXPRESS = 'PCIE'
    INTERFACE_CHOICES = (
        (IDE, 'IDE'),
        (SATA, 'SATA'),
        (SAS, 'SAS'),
        (USB, 'USB'),
        (FIREWIRE, 'FireWire'),
        (THUNDERBOLT, 'Thunderbolt'),
        (PCI_EXPRESS, 'PCIe'),
    )

    ONE_POINT_EIGHT = '1.8'
    TWO_POINT_FIVE = '2.5'
    THREE_POINT_FIVE = '3.5'
    FORM_FACTOR_CHOICES = (
        (ONE_POINT_EIGHT, '1.8"'),
        (TWO_POINT_FIVE, '2.5"'),
        (THREE_POINT_FIVE, '3.5"'),
    )

    id = models.BigIntegerField(primary_key=True, default=generate_id)
    host = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    serial = models.CharField(max_length=100, blank=True)
    capacity = models.BigIntegerField(blank=True, null=True)  # stored as bytes
    media_type = models.CharField(max_length=4,
                                  blank=True, choices=MEDIA_TYPE_CHOICES)
    interface = models.CharField(max_length=4,
                                 blank=True, choices=INTERFACE_CHOICES)
    form_factor = models.CharField(max_length=3,
                                   blank=True, choices=FORM_FACTOR_CHOICES)
    rpm = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True)
    in_use = models.NullBooleanField(blank=True)
    status = models.NullBooleanField(blank=True)
    purchase_date = models.DateTimeField(blank=True, null=True)
    warranty_date = models.DateTimeField(blank=True, null=True)
    service_start_date = models.DateTimeField(blank=True, null=True)
    service_end_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def get_capacity_representation(self):
        """
        Converts the capacity in bytes to the appropriate value for display
        """
        if not self.capacity:
            return''
        return (bitmath.Byte(self.capacity)
                .best_prefix(bitmath.SI)
                .format("{value} {unit}"))

    def get_in_use_representation(self):
        """Converts the in_use boolean to a yes/no for display"""
        return 'Yes' if self.in_use else 'No'
