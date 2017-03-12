from django import forms
from .models import TestTab

class TestTabForm(forms.ModelForm):
    i_check = forms.BooleanField(initial=False, required=False)
    fild_names = ['foo','bar'] 
    class Meta:
        model = TestTab
        fields = [] 

#    def __new__(cls, *args, **kwargs):
#        super(TestTabForm, cls).__new__(*args, **kwargs)
#        cls.fields['boo'] = forms.IntegerField(label="boo")

    def __init__(self, *args, **kwargs):
        super(TestTabForm, self).__init__(*args, **kwargs)
        self.fields['foo'] = forms.IntegerField(label="foo")
        self.fields['bar'] = forms.IntegerField(label="bar")
