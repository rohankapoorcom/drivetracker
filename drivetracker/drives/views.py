from crispy_forms.utils import render_crispy_form
from dal import autocomplete
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import csrf
from jsonview.decorators import json_view
from rest_framework import generics

import drivetracker.drives.models as models
from drivetracker.drives.forms import HardDriveForm
from drivetracker.drives.serializers import HardDriveSerializer


class HardDriveList(generics.ListAPIView):
    queryset = models.HardDrive.objects.all()
    serializer_class = HardDriveSerializer

    def get_serializer_context(self, **kwargs):
        context = super(HardDriveList, self).get_serializer_context(**kwargs)
        context['representation'] = self.request.GET.get('representation')
        return context


class HardDriveDetail(generics.RetrieveDestroyAPIView):
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
def edit_hard_drive_view(request, pk=None):
    if pk is not None:
        hd = get_object_or_404(models.HardDrive, pk=pk)
    else:
        hd = None

    ctx = {}
    ctx.update(csrf(request))

    if request.method == 'POST':
        hard_drive_form = HardDriveForm(request.POST or None, instance=hd)
        if hard_drive_form.is_valid():
            hard_drive_form.save()
            return {'success': True}

        form_html = render_crispy_form(hard_drive_form, context=ctx)
        return {'success': False, 'form_html': form_html}

    elif request.method == 'GET':
        hard_drive_form = HardDriveForm(instance=hd)
        form_html = render_crispy_form(hard_drive_form, context=ctx)
        return {'form_html': form_html}
