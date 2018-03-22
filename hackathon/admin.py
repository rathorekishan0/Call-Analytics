from django.contrib import admin
from . import models
admin.site.register(models.Recordings)
admin.site.register(models.Staff)
admin.site.register(models.Customer)
admin.site.register(models.Score)

