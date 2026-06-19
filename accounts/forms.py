from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Role


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    location = forms.CharField(max_length=100, required=True)
    role = forms.ChoiceField(choices=[
        (Role.FARMER, 'Farmer'),
        (Role.BUYER,  'Buyer'),
    ])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone',
                  'location', 'role', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email',
                  'phone', 'location', 'profile_photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name':  forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email':      forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'phone':      forms.TextInput(attrs={'placeholder': 'e.g. 0712345678'}),
            'location':   forms.TextInput(attrs={'placeholder': 'e.g. Nakuru'}),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model  = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'location', 'profile_photo']