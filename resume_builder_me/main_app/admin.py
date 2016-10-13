from django.contrib import admin
from .models import Resume, Project, Gpa
# Register your models here.

#class GpaInlineAdmin(admin.TabularInline):
#	model = Gpa
#	can_delete = False

myModels = [Resume, Project, Gpa]
admin.site.register(myModels)

# Register your models here.
