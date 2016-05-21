from django.contrib import admin

import drivetracker.drives.models as models

# Register your models here.
admin.site.register(models.Host)
admin.site.register(models.Manufacturer)
admin.site.register(models.Model)
admin.site.register(models.HardDrive)
