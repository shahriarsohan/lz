from django import forms

from django.contrib.auth.models import User
from .models import UserProfile


class UpdateUserForm(forms.ModelForm):
    f_name = forms.CharField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    l_name = forms.CharField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['f_name', 'l_name', 'email']
