from django.contrib import admin
from Institute.models import ServicesData

class Services(admin.ModelAdmin):
    list_display = (
        'cno',
        'cname',
        'faculty',
        'duration',
        'fees',
        'content',
    )
admin.site.register(ServicesData,Services)