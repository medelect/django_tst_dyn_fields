from django.contrib import admin

from .forms import TestTabForm
from .models import TestTab

class TestTabAdmin(admin.ModelAdmin):
    list_display = ['name','numb']
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 25
    form = TestTabForm
    fieldsets = (
            (None, {
              'fields': (('name'),)
             }),
            (None, {
                'fields': (('numb'),),
                'classes': (('collapse',),)
            }),
            )
    
admin.site.register(TestTab, TestTabAdmin)
