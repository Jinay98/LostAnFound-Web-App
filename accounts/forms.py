from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    last_name = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    UID = forms.IntegerField(required=True, help_text='Compulsory Field')
    Branch = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
    Year = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
    ContactNo = forms.IntegerField(required=True, help_text='Compulsory Field')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

# class UserProfileForm(forms.ModelForm):
#     UID = forms.IntegerField(required=True, help_text='Compulsory Field',)
#     Branch = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
#     Year = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
#     ContactNo = forms.IntegerField(required=True, help_text='Compulsory Field')
#     class Meta:
#          model = UserProfile
#          fields = ('UID','Branch','Year','ContactNo')