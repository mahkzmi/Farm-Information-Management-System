from django import forms
from .models import Field, Crop, Activity

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['name', 'area', 'soil_type', 'planting_date']
        widgets = {
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'field', 'planting_date', 'harvest_date', 'yield_amount']
        widgets = {
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
            'harvest_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['field', 'activity_type', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }