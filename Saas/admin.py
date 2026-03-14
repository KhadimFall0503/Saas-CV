from django.contrib import admin
from .models import CV

# Register your models here.
class CVAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone')
admin.site.register(CV, CVAdmin)