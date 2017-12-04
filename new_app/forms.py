from django import forms
from .models import DataCollection

class AddNumbersForm(forms.ModelForm):
    class Meta:
        model = DataCollection
        fields = [
            'numbers'
        ]