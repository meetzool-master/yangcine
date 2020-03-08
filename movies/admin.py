from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
    pass



@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    pass    
    