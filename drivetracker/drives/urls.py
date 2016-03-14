from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

import drivetracker.drives.views as views

urlpatterns = [
    url(r'^$', views.home, name='drives_home'),
    url(r'^api/drives/$', views.HardDriveList.as_view(),
        name='api_drives_list'),
    url(r'^api/drives/(?P<pk>[0-9]+)/$', views.HardDriveDetail.as_view(),
        name='api_drives_detail'),
    url(r'^api/drives/form/(?:/(?P<pk>[0-9]+)/)?$', views.edit_hard_drive_view,
        name='api_drives_form'),
    url(r'^api/drives/autocomplete/hosts/$',
        views.HostAutoComplete.as_view(create_field='name'),
        name='api_drives_autocomplete_hosts'),
    url(r'^api/drives/autocomplete/manufacturers/$',
        views.ManufacturerAutoComplete.as_view(create_field='name'),
        name='api_drives_autocomplete_manufacturers'),
    url(r'^api/drives/autocomplete/models/$',
        views.ModelAutoComplete.as_view(create_field='name'),
        name='api_drives_autocomplete_models'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
