from django import forms
from .models import Produce


class ProduceForm(forms.ModelForm):
    class Meta:
        model = Produce
        fields = [
            'name', 'category', 'quantity',
            'unit', 'price', 'location',
            'description', 'image'
        ]
        widgets = {
            'name':        forms.TextInput(attrs={'placeholder': 'e.g. Maize, Tomatoes'}),
            'quantity':    forms.NumberInput(attrs={'placeholder': 'e.g. 100'}),
            'unit':        forms.TextInput(attrs={'placeholder': 'e.g. kg, crate, bag'}),
            'price':       forms.NumberInput(attrs={'placeholder': 'Price per unit in KES'}),
            'location':    forms.TextInput(attrs={'placeholder': 'e.g. Nakuru, Nyeri'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional details about your produce...'}),
        }
