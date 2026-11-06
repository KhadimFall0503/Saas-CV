from django.contrib import admin
from .models import CV, TemplateCV

# Register your models here.
class CVAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone')
admin.site.register(CV, CVAdmin)

class TemplateCVAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_popular', 'is_new')
admin.site.register(TemplateCV, TemplateCVAdmin)