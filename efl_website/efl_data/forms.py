from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewEmployee

class UserRegisterForm(UserCreationForm):
    dob = forms.DateField(required=True)
    surname = forms.CharField(max_length=255, required=True)
    forename = forms.CharField(max_length=255, required=True)
    title = forms.CharField(max_length=255, required=True)
    postcode = forms.CharField(max_length=255, required=True)
    add1 = forms.CharField(max_length=255, required=True)
    add2 = forms.CharField(max_length=255, required=True)
    employee = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    role = forms.ChoiceField(choices=NewEmployee.ROLE_CHOICES)
    
    class Meta:
        model = NewEmployee
        fields = ['forename', 'surname', 'email', 'password1', 'password2', 'dob', 'title', 'postcode', 'add1', 'employee', 'add2', 'role']

class LoginForm(forms.Form):
    employee = forms.CharField(widget=forms.TextInput(attrs={'class': 'employee-entry'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-entry'}))
