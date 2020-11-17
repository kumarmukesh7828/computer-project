from django import forms
from webapp.models import Computer


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'

class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name','user_name']
