from django.shortcuts import render
from django.core.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from jsonview.decorators import json_view
from rest_framework import generics

from drivetracker.drives.models import HardDrive
from drivetracker.drives.serializers import HardDriveSerializer
from drivetracker.drives.forms import HardDriveForm


class HardDriveList(generics.ListAPIView):
    queryset = HardDrive.objects.all()
    serializer_class = HardDriveSerializer

    def get_serializer_context(self, **kwargs):
        context = super(HardDriveList, self).get_serializer_context(**kwargs)
        context['representation'] = self.request.GET.get('representation')
        return context


class HardDriveDetail(generics.RetrieveAPIView):
    queryset = HardDrive.objects.all()
    serializer_class = HardDriveSerializer

    def get_serializer_context(self, **kwargs):
        context = super(HardDriveDetail, self).get_serializer_context(**kwargs)
        context['representation'] = self.request.GET.get('representation')
        return context


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
