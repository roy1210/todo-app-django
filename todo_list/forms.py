from django import  forms
# Use List DB
from .models import  List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        # Refer from models.py
        fields = ["item", "completed"]