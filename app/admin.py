from django.contrib import admin

from app import models

admin.site.register(models.Director)
admin.site.register(models.Film)
admin.site.register(models.People)
admin.site.register(models.Planet)
admin.site.register(models.Producer)
