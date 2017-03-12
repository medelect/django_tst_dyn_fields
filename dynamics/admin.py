from django.contrib import admin

from .forms import TestTabForm
from .models import TestTab

from django.contrib.admin.utils import flatten_fieldsets

class TestTabAdmin(admin.ModelAdmin):
#    list_display = ['name','numb']
#    search_fields = ('name',)
#    ordering = ('name',)
    list_per_page = 25
    form = TestTabForm
#    fields = ['name', 'numb']

    fieldsets = (
            (None, {
              'fields': ['numb']
             }),
            ('Additional',{'fields':['i_check']})
            )
#    def get_fieldsets(self, request, obj=None):
#        fields = super(TestTabAdmin, self).get_fieldsets(request, obj)
#        fieldsets[0][1]['fields'] += ['foo'] 
#        return fieldsets
    def get_form(self, request, obj=None, **kwargs):
        for i in dir(self): print i
        print "@@@@@@@@@@@"
        print "!!!",' |self.form:   ', type(self.form)
        for i in dir(self.form):print i
        print "!!!",' |self.form.Meta:   ', type(self.form.Meta)
        for i in dir(self.form.Meta):print i
        print "!!!",' |self.form.Meta.fields:   ', self.form.Meta.fields
 

#        print "!!!",' |self.formfield_for_choice_field:   ',\
#                self.formfield_for_choice_field()
#        print "!!!",' |self.formfield_for_dbfield:   ',\
#                type(self.formfield_for_dbfield)
#        print "!!!",' |self.formfield_for_foreignkey:   ',\
#                type(self.formfield_for_foreignkey)
#        print "!!!",' |self.formfield_for_manytomany:   ',\
#                type(self.formfield_for_manytomany)
#        print "!!!",' |self.formfield_overrides:   ',\
#                type(self.formfield_overrides)
#        print '!!!', ' self.form ', dir(self.form)
#        print '!!!!!!!!', ' self.form ', self.form.declared_fields
#        print '!!!!!!!!', ' self.clean ', type(self.form)



        kwargs['fields'] =  flatten_fieldsets(self.fieldsets)
        return super(TestTabAdmin, self).get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(TestTabAdmin, self).get_fieldsets(request, obj)

        newfieldsets = list(fieldsets)
        fields = ['bar', 'foo']
        newfieldsets.append(['Dynamic Fields', { 'fields': fields }])

        return newfieldsets

admin.site.register(TestTab, TestTabAdmin)
