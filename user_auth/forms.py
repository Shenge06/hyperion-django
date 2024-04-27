from django import forms
from django.contrib.auth.models import User

# Define a custom form class named SignUpForm that inherits from forms.ModelForm
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        # Meta class contains metadata about the form
        model = User
        fields = ['username', 'password', 'email']  # Add or remove fields as needed
