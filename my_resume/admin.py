from django.contrib import admin
from . import models

admin.site.register(models.Resume)
admin.site.register(models.Education)
admin.site.register(models.Achievements)
admin.site.register(models.Project)
admin.site.register(models.Skills)
admin.site.register(models.Contact)
