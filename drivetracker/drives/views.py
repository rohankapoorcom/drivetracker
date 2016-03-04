from django.shortcuts import render

from drivetracker.drives.models import HardDrive
from drivetracker.drives.serializers import HardDriveSerializer
from rest_framework import generics


class HardDriveList(generics.ListAPIView):
    queryset = HardDrive.objects.all()
    serializer_class = HardDriveSerializer


class HardDriveDetail(generics.RetrieveAPIView):
    queryset = HardDrive.objects.all()
    serializer_class = HardDriveSerializer
