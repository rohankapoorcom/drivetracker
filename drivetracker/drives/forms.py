from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete

import drivetracker.drives.models as models


class HardDriveForm(ModelForm):

    class Meta:
        model = models.HardDrive
        fields = ['host', 'manufacturer', 'model', 'serial', 'capacity',
                  'media_type', 'interface', 'form_factor', 'rpm', 'position',
                  'in_use', 'status', 'purchase_date', 'warranty_date',
                  'service_start_date', 'service_end_date', 'notes']
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
