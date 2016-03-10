from django.shortcuts import render
from django.core.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from jsonview.decorators import json_view
from rest_framework import generics
from dal import autocomplete

from drivetracker.drives.serializers import HardDriveSerializer
from drivetracker.drives.forms import HardDriveForm
import drivetracker.drives.models as models


class HardDriveList(generics.ListAPIView):
    queryset = models.HardDrive.objects.all()
    serializer_class = HardDriveSerializer

    def get_serializer_context(self, **kwargs):
        context = super(HardDriveList, self).get_serializer_context(**kwargs)
        context['representation'] = self.request.GET.get('representation')
        return context


class HardDriveDetail(generics.RetrieveAPIView):
    queryset = models.HardDrive.objects.all()
    serializer_class = HardDriveSerializer

    def get_serializer_context(self, **kwargs):
        context = super(HardDriveDetail, self).get_serializer_context(**kwargs)
        context['representation'] = self.request.GET.get('representation')
        return context


class HostAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        queryset = models.Host.objects.all()

        if self.q:
            queryset = queryset.filter(name__istartswith=self.q)
        return queryset

    def has_add_permission(self, request):
        return True


class ManufacturerAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        queryset = models.Manufacturer.objects.all()

        if self.q:
            queryset = queryset.filter(name__istartswith=self.q)
        return queryset

    def has_add_permission(self, request):
        return True


class ModelAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        queryset = models.Model.objects.all()

        if self.q:
            queryset = queryset.filter(name__istartswith=self.q)
        return queryset

    def has_add_permission(self, request):
        return True


def home(request):
    hard_drive_form = HardDriveForm()
    return render(request, 'home.html', {'hard_drive_form': hard_drive_form})


@json_view
def save_hard_drive_form(request):
    hard_drive_form = HardDriveForm(request.POST or None)
    if hard_drive_form.is_valid():
        hard_drive_form.save()
        return {'success': True}

    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(hard_drive_form, context=ctx)
    return {'success': False, 'form_html': form_html}
