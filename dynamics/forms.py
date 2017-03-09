from django import forms
from .models import TestTab

class TestTabForm(forms.ModelForm):
    i_check = forms.BooleanField(initial=False, required=False)
    class Meta:
        model = TestTab
        fields = '__all__'

