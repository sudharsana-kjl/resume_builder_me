from django.contrib import admin
from .models import Resume, Project
# Register your models here.
myModels = [Resume, Project]
admin.site.register(myModels)

# Register your models here.
