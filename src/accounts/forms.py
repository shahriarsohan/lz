from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from accounts.models import CustomUser


class MyCustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True,
                             help_text='Required. Inform a valid email address.')
    fullname = forms.CharField(max_length=30)
    phone = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'fullname',
                  'phone', 'password1', 'password2', )
