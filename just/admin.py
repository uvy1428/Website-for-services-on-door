from django.contrib import admin
from . import models

myModels = [models.Details, models.Price, models.Form]  # iterable list
admin.site.register(myModels)
