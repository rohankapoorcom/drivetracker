from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

import drivetracker.drives.views as views

urlpatterns = [
    url(r'^$', views.home, name='drives_home'),
    url(r'^api/drives/$', views.HardDriveList.as_view(),
        name='api_drives_list'),
    url(r'^api/drives/(?P<pk>[0-9]+)/$', views.HardDriveDetail.as_view(),
        name='api_drives_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
