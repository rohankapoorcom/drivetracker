from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from dal import autocomplete

import drivetracker.drives.models as models
import bitmath


def get_capacity_units():
    return [('{}B'.format(prefix),
             '{}B'.format(prefix)) for prefix in bitmath.SI_PREFIXES]


class HardDriveForm(ModelForm):
    unit = forms.ChoiceField(choices=get_capacity_units())

    class Meta:
        model = models.HardDrive
        fields = ['host', 'manufacturer', 'model', 'serial', 'capacity',
                  'unit', 'media_type', 'interface', 'form_factor', 'rpm',
                  'position', 'in_use', 'status', 'purchase_date',
                  'warranty_date', 'service_start_date', 'service_end_date',
                  'notes']
        widgets = {
            'host': autocomplete.ModelSelect2(
                url='api_drives_autocomplete_hosts'),
            'manufacturer': autocomplete.ModelSelect2(
                url='api_drives_autocomplete_manufacturers'),
            'model': autocomplete.ModelSelect2(
                url='api_drives_autocomplete_models'),
        }

    def __init__(self, *args, **kwargs):
        super(HardDriveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_id = 'hard-drive-form'
        self.helper.include_media = False

    def clean(self):
        cleaned_data = super(HardDriveForm, self).clean()
        capacity = cleaned_data.get('capacity', 0)
        unit = cleaned_data.get('unit', '')
        obj = bitmath.parse_string('{}{}'.format(capacity, unit))
        cleaned_data['capacity'] = obj.to_Byte().value
        return cleaned_data
